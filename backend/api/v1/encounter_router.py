from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from typing_extensions import Annotated

from encounter.dependencies import get_encounter_service
from encounter.schemas import EncounterSchema
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


@router.post(path="/encounter/create", response_model=EncounterSchema, tags=["encounter"])
async def create_encounter(
        service: Annotated[EncounterService, Depends(get_encounter_service)],
):
    encounter = await service.create_encounter()
    return encounter
