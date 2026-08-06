from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import AsyncGenerator, Annotated

from database_core import new_session
from encounter.repository import EncounterRepo
from encounter.service import EncounterService


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session

async def get_encounter_repo(session: Annotated[AsyncSession, Depends(get_db)]) -> EncounterRepo:
    return EncounterRepo(session=session)

async def get_encounter_service(repo: Annotated[EncounterRepo, Depends(get_encounter_repo)]) -> EncounterService:
    return EncounterService(repository=repo)
