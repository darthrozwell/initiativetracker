from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from src.dependencies import get_db
from src.encounter.service import EncounterService


async def get_encounter_service(session: Annotated[AsyncSession, Depends(get_db)]) -> EncounterService:
    return EncounterService(session=session)
