from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Body
from typing import List

from starlette import status
from typing_extensions import Annotated

from src.encounter.exceptions import AddEncFailedError, DeleteEncFailedError, DeleteEncNotFoundError, UpdateEncFailedError, \
    AddCombFailedError, UpdateCombFailedError, DeleteCombFailedError, DeleteCombNotFoundError, CombatantHasNoTypeError
from src.encounter.dependencies import get_encounter_service
from src.encounter.schemas import EncounterInSchema, EncounterOutSchema, \
    CombatantInSchema, CombatantUpdateSchema, EncounterUpdateSchema, CombatantOutMonsterSchema, \
    CombatantOutCharacterSchema
from src.encounter.service import EncounterService

router = APIRouter()


@router.get(path="/{encounter_id}", response_model=EncounterOutSchema, status_code=status.HTTP_200_OK)
async def get_encounter(
        encounter_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    encounter = await service.get_encounter(encounter_id)
    if not encounter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Encounter not found")
    return encounter


@router.get(path="/", response_model=List[EncounterOutSchema], status_code=status.HTTP_200_OK)
async def get_all_encounters(
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    encounters = await service.get_all_encounters()
    if not encounters:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no encounters found")
    return encounters


@router.post(path="/", response_model=EncounterOutSchema, status_code=status.HTTP_201_CREATED)
async def create_encounter(
        encounter: Annotated[EncounterInSchema, Body(embed=True)],
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    try:
        encounter = await service.create_encounter(encounter)
    except AddEncFailedError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Encounter already exists")
    return encounter


@router.delete(path="/{encounter_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_encounter(
        encounter_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    try:
        await service.delete_encounter(encounter_id=encounter_id)
    except DeleteEncNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Encounter not found")
    except DeleteEncFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Something went wrong")
    return


@router.put(path="/{encounter_id}", status_code=status.HTTP_200_OK)
async def update_encounter(
        encounter_id: str,
        encounter: Annotated[EncounterUpdateSchema, Body(embed=True)],
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    try:
        result = await service.update_encounter(encounter_id=encounter_id, encounter=encounter)
    except UpdateEncFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Something went wrong")
    return


@router.get(path="/{encounter_id}/combatant", response_model=list[CombatantOutMonsterSchema | CombatantOutCharacterSchema], status_code=status.HTTP_200_OK)
async def get_combatants(
        encounter_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    try:
        combatants = await service.get_combatants(encounter_id=encounter_id)
    except CombatantHasNoTypeError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Bad combatant data on server")
    if not combatants:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Combatants not found")
    return combatants


@router.post(path="/{encounter_id}/combatant", response_model=CombatantOutMonsterSchema | CombatantOutCharacterSchema, status_code=status.HTTP_201_CREATED)
async def create_combatant(
        encounter_id: str,
        combatant: Annotated[CombatantInSchema, Body(embed=True)],
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    try:
        combatant = await service.create_combatant(encounter_id=encounter_id, combatant_in=combatant)
    except CombatantHasNoTypeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Combatant has no type")
    except AddCombFailedError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Combatant already exists")
    return combatant


@router.put(path="/{encounter_id}/combatant/{combatant_id}", status_code=status.HTTP_200_OK)
async def update_combatant(
        combatant_id: str,
        combatant: Annotated[CombatantUpdateSchema, Body(embed=True)],
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    try:
        await service.update_combatant(combatant_id=combatant_id, new_schema=combatant)
    except UpdateCombFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Something went wrong")
    return


@router.delete(path="/{encounter_id}/combatant/{combatant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_combatant(
        combatant_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    try:
        await service.delete_combatant(combatant_id=combatant_id)
    except DeleteCombNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Combatant not found")
    except DeleteCombFailedError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Something went wrong")
    return
