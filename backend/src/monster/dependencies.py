from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from src.dependencies import get_db
from src.monster.service import MonsterService



async def get_monster_service(session: Annotated[AsyncSession, Depends(get_db)]) -> MonsterService:
    return MonsterService(session=session)
