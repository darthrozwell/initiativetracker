from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from src.dependencies import get_db
from src.character.service import CharacterService



async def get_character_service(session: Annotated[AsyncSession, Depends(get_db)]) -> CharacterService:
    return CharacterService(session=session)
