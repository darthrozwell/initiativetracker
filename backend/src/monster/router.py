import json
from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, status
from pydantic import TypeAdapter
from typing_extensions import Annotated

from src.monster.dependencies import get_monster_service
from src.monster.exceptions import AddFailedError, AddAttackFailedError, UpdateFailedError, UpdateAttackFailedError, \
    DeleteFailedError, DeleteNotFoundError
from src.monster.schemas import MonsterInSchema, MonsterOutSchema
from src.monster.service import MonsterService

router = APIRouter()


@router.get(path="/{monster_name}", response_model=MonsterOutSchema, status_code=status.HTTP_200_OK)
async def get_monster_by_name(
        monster_name: str,
        service: Annotated[MonsterService, Depends(get_monster_service)]
):
    monster = await service.get_by_name(name=monster_name)
    if monster is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Monster not found")
    return monster


@router.get(path="/", response_model=list[MonsterOutSchema], status_code=status.HTTP_200_OK)
async def get_all_monsters(
        service: Annotated[MonsterService, Depends(get_monster_service)]
):
    monsters = await service.get_all()
    if not monsters:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Monster not found")
    return monsters


@router.post(path="/", response_model=MonsterOutSchema, status_code=status.HTTP_201_CREATED)
async def post_monster(
        monster: Annotated[MonsterInSchema, Body(embed=True)],
        service: Annotated[MonsterService, Depends(get_monster_service)],
):
    try:
        new_monster = await service.add(monster_schema=monster)
    except AddFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Monster violates database constraints")
    except AddAttackFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Monster attack violates database constraints")
    return new_monster


@router.post(path="/upload", status_code=status.HTTP_201_CREATED)
async def upload_monster(
        file: UploadFile,
        service: Annotated[MonsterService, Depends(get_monster_service)],
):
    data = json.loads(await file.read())
    await file.close()
    monsters = TypeAdapter(list[MonsterInSchema]).validate_python(data)
    for monster in monsters:
        try:
            await service.add(monster)
        except UpdateFailedError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Monster violates database constraints")
        except AddAttackFailedError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Monster attack violates database constraints")
    return {"count": len(monsters)}


@router.put(path="/{monster_id}", status_code=status.HTTP_200_OK)
async def update_monster(
        monster_id: str,
        monster: Annotated[MonsterInSchema, Body(embed=True)],
        service: Annotated[MonsterService, Depends(get_monster_service)],
):
    try:
        await service.update(monster_id, monster)
    except UpdateFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Monster violates database constraints")
    except UpdateAttackFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Monster attack violates database constraints")
    return


@router.delete(path="/{monster_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_monster(
        monster_id: str,
        service: Annotated[MonsterService, Depends(get_monster_service)],
):
    try:
        await service.delete(monster_id)
    except DeleteFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Monster cannot be deleted")
    except DeleteNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Monster not found")
    return
