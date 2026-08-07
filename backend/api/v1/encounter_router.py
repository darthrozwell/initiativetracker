from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Body
from typing_extensions import Annotated

from encounter.dependencies import get_encounter_service
from encounter.schemas import EncounterSchema, EncounterUpdateSchema, CombatantSchema
from encounter.service import EncounterService

router = APIRouter()


@router.get(path="/encounter/{encounter_id}", response_model=EncounterSchema, tags=["encounter"])
async def get_encounter(
        encounter_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    encounter = await service.get_encounter(encounter_id)
    if encounter is None:
        raise HTTPException(status_code=404, detail="Encounter not found")
    return encounter


@router.get(path="/encounters", response_model=List[EncounterSchema], tags=["encounter"])
async def get_all_encounters(
service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    encounters = await service.get_all_encounters()
    if encounters is None:
        raise HTTPException(status_code=404, detail="There is no encounters found")
    return encounters


@router.post(path="/encounter", response_model=EncounterSchema, tags=["encounter"])
async def create_encounter(
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    encounter = await service.create_encounter()
    return encounter


@router.delete(path="/encounter/{encounter_id}", tags=["encounter"])
async def delete_encounter(
        encounter_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    await service.delete_encounter(encounter_id=encounter_id)
    return {"message": "Encounter deleted successfully"}


@router.put(path="/encounter/{encounter_id}", tags=["encounter"])
async def update_encounter(
        encounter_id: str,
        encounter: Annotated[EncounterUpdateSchema, Body(embed=True)],
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    await service.update_encounter(encounter_id=encounter_id, encounter=encounter)
    return {"message": "Encounter updated successfully"}


@router.get(path="/encounter/{encounter_id}/combatants", response_model=list[CombatantSchema], tags=["combatants"])
async def get_combatants(
        encounter_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    combatants = await service.get_combatants(encounter_id=encounter_id)
    return combatants

@router.post(path="/encounter/{encounter_id}/combatant", response_model=CombatantSchema, tags=["combatants"])
async def create_combatant(
        encounter_id: str,
        combatant: Annotated[CombatantSchema, Body(embed=True)],
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    combatant = await service.create_combatant(encounter_id=encounter_id, combatant=combatant)
    return combatant

@router.put(path="/encounter/{encounter_id}/combatant/{combatant_id}", tags=["combatants"])
async def update_combatant(
        combatant: Annotated[CombatantSchema, Body(embed=True)],
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    await service.update_combatant(combatant=combatant)
    return

@router.delete(path="/encounter/{encounter_id}/combatant/{combatant_id}", tags=["combatants"])
async def delete_combatant(
        combatant_id: str,
        service: Annotated[EncounterService, Depends(get_encounter_service)]
):
    await service.delete_combatant(combatant_id=combatant_id)
    return {"message": "Combatant deleted successfully"}
