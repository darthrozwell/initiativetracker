import uuid
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.monster.exceptions import AddFailedError, AddAttackFailedError, UpdateFailedError, UpdateAttackFailedError, \
    DeleteFailedError, DeleteNotFoundError
from src.monster.models import MonsterModel, MonsterAttackModel
from src.monster.schemas import MonsterInSchema


class MonsterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_name(self, name: str) -> MonsterModel | None:
        query = select(MonsterModel).where(MonsterModel.name == name)
        result = await self.session.execute(query)
        return result.scalars().first()


    async def get_all(self):
        query = select(MonsterModel).order_by(MonsterModel.name)
        result = await self.session.execute(query)
        return result.scalars().all()


    async def add(self, monster_schema: MonsterInSchema):
        new_monster = MonsterModel(**monster_schema.model_dump(exclude={"abilities"}))
        new_monster.monster_id = str(uuid.uuid4())
        self.session.add(new_monster)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddFailedError
        if monster_schema.abilities is not None:
            for data_abilities in monster_schema.abilities:
                new_ability = MonsterAttackModel(**data_abilities.model_dump())
                new_ability.attack_id = str(uuid.uuid4())
                new_ability.monster_name = new_monster.name
                self.session.add(new_ability)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddAttackFailedError
        return new_monster


    async def update(self, monster_id: str, monster_schema: MonsterInSchema):
        data = monster_schema.model_dump(exclude={"abilities"})
        query = update(MonsterModel).where(MonsterModel.monster_id == monster_id).values(**data)
        await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateFailedError
        if monster_schema.abilities is not None:
            for data_abilities in monster_schema.abilities:
                query = update(MonsterAttackModel).where(MonsterAttackModel.monster_name == monster_schema.name).values(**data_abilities.model_dump())
                result = await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateAttackFailedError
        return


    async def delete(self, monster_id: str):
        query = select(MonsterModel).where(MonsterModel.monster_id == monster_id).with_for_update()
        result = await self.session.execute(query)
        monster = result.scalar_one_or_none()
        if monster is None:
            raise DeleteNotFoundError
        try:
            await self.session.delete(monster)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise DeleteFailedError
