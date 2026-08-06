from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from monster.models import Base

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:6432/postgres"

engine = create_async_engine(url=DATABASE_URL)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)

async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
