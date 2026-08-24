from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.models_core import Base
from src.settings import settings


engine = create_async_engine(url=settings.database_url, echo=settings.debug)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)

async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
