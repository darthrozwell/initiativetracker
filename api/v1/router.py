from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from typing_extensions import Annotated

from monster.dependencies import get_monster_service
from monster.models import MonsterModel
from monster.schemas import Monster as MonsterSchema
from monster.service import MonsterService

router = APIRouter()


@router.get("/monster/", response_model=MonsterSchema)
async def get_monster(
        monster_name: Annotated[str, Query(min_length=2, max_length=50, example="Alohomora")],
        service: Annotated[MonsterService, Depends(get_monster_service)]
) -> MonsterModel | None:
    monster = await service.get_by_name(name=monster_name)

    if monster is None:
        raise HTTPException(status_code=404, detail="Monster not found")

    return monster

@router.post("/monster/")
async def post_monster(
        monster: MonsterSchema,
        service: Annotated[MonsterService, Depends(get_monster_service)]
) -> None:
    response = await service.add_monster(name=monster.name)
    return
