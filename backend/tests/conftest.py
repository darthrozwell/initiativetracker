from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import pytest_asyncio
from typing_extensions import AsyncGenerator

from src.encounter.models import EncounterModel, CombatantModel
from src.monster.models import MonsterModel
from src.dependencies import get_db
from src.models_core import Base
from src.main import app

engine = create_async_engine(
    url='postgresql+asyncpg://postgres:postgres@localhost:7432/postgres_test'
)
new_test_session = async_sessionmaker(bind=engine, expire_on_commit=False)


@pytest_asyncio.fixture()
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest_asyncio.fixture
async def test_db_session(setup_db):
    async with new_test_session() as session:
        yield session

@pytest_asyncio.fixture(scope="function")
async def client(test_db_session):
    async def override_get_db():
        yield test_db_session
    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client

@pytest_asyncio.fixture(autouse=True)
async def create_default_monster(test_db_session):
   monster=MonsterModel(**{
            "monster_id": "test_monster_id",
            "name": "test_monster_name",
            "source": "Custom",
            "size": "Средний",
            "creature_type": "Гуманоид",
            "alignment": "Нейтральный",
            "armor_class": 1,
            "initiative": 1,
            "hit_points_value": 1,
            "hit_points_formula": "string",
            "speed": "string",
            "skills": "string",
            "damage_resistance": "string",
            "damage_immunity": "string",
            "damage_vulnerability": "string",
            "senses": "string",
            "languages": "string",
            "challenge_rating": "string",
            "experience": 1,
            "proficiency_bonus": 1,
            "equipment": "string",
            "treasure": "string",
            "habitat": "string",
            "strength_value": 10,
            "strength_mod": 0,
            "strength_save": 0,
            "dexterity_value": 10,
            "dexterity_mod": 0,
            "dexterity_save": 0,
            "constitution_value": 10,
            "constitution_mod": 0,
            "constitution_save": 0,
            "intelligence_value": 10,
            "intelligence_mod": 0,
            "intelligence_save": 0,
            "wisdom_value": 10,
            "wisdom_mod": 0,
            "wisdom_save": 0,
            "charisma_value": 10,
            "charisma_mod": 0,
            "charisma_save": 0,


   }
                        )
   test_db_session.add(monster)
   await test_db_session.commit()
   await test_db_session.refresh(monster)
   return monster


@pytest_asyncio.fixture(autouse=True)
async def create_test_encounter(test_db_session):
    encounter=EncounterModel(**{
                "encounter_id": "test_encounter_id",
                "name": "test_encounter_name",
                "round": 1,
                "current_turn": 0
              })
    test_db_session.add(encounter)
    await test_db_session.commit()
    await test_db_session.refresh(encounter)

    combatant=CombatantModel(**{
                                    "combatant_id": "test_combatant_id",
                                    "encounter_id": "test_encounter_id",
                                    "monster_id": "test_monster_id",
                                    "nickname": "test_nickname",
                                    "current_hp": 0,
                                    "status": "alive"})
    test_db_session.add(combatant)
    await test_db_session.commit()
    await test_db_session.refresh(combatant)
    print(combatant.combatant_id)

    return encounter
