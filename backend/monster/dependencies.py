from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import AsyncGenerator, Annotated

from database_core import new_session
from monster.repository import MonsterRepo
from monster.service import MonsterService


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session

async def get_monster_repo(session: Annotated[AsyncSession, Depends(get_db)]) -> MonsterRepo:
    return MonsterRepo(session=session)

async def get_monster_service(repo: Annotated[MonsterRepo, Depends(get_monster_repo)]) -> MonsterService:
    return MonsterService(repository=repo)
