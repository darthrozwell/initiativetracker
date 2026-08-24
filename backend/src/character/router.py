from fastapi import APIRouter, Depends, HTTPException, Body
from starlette import status
from typing_extensions import Annotated

from src.character.exceptions import DeleteCharacterNotFoundError
from src.character.dependencies import get_character_service
from src.character.exceptions import AddCharacterFailedError, UpdateCharacterFailedError, DeleteCharacterFailedError
from src.character.schemas import CharacterOutSchema, CharacterInSchema, CharacterUpdateSchema
from src.character.service import CharacterService

router = APIRouter()


@router.get("/", response_model=list[CharacterOutSchema], status_code=status.HTTP_200_OK)
async def get_all_characters(
        service: Annotated[CharacterService, Depends(get_character_service)],
):
    try:
        characters = await service.get_all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not characters:
        return [] #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No characters found")
    return characters


@router.get("/{character_id}", response_model=CharacterOutSchema, status_code=status.HTTP_200_OK)
async def get_character(
        character_id: str,
        service: Annotated[CharacterService, Depends(get_character_service)],
):
    try:
        character = await service.get_by_id(character_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    if not character:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
    return character


@router.post("/", response_model=CharacterOutSchema, status_code=status.HTTP_201_CREATED)
async def create_character(
        character: Annotated[CharacterInSchema, Body(embed=True)],
        service: Annotated[CharacterService, Depends(get_character_service)],
):
    try:
        new_character = await service.create(character=character)
    except AddCharacterFailedError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Character already exists")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return new_character


@router.put("/{character_id}", status_code=status.HTTP_200_OK)
async def update_character(
        character_id: str,
        data: Annotated[CharacterUpdateSchema, Body(embed=True)],
        service: Annotated[CharacterService, Depends(get_character_service)],
):
    try:
        await service.update(character_id=character_id, data=data)
    except UpdateCharacterFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Smth bad with data")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return


@router.delete("/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_character(
        character_id: str,
        service: Annotated[CharacterService, Depends(get_character_service)],
):
    try:
        await service.delete(character_id=character_id)
    except DeleteCharacterNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found")
    except DeleteCharacterFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Smth went wrong")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return
