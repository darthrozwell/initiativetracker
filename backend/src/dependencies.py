from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import AsyncGenerator

from src.database_core import new_session


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session
