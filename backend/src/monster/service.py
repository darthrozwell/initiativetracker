from uuid import UUID
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.action.models import AbilityModel
from src.monster.models import MonsterModel
from src.monster.schemas import MonsterInSchema, MonsterUpdateSchema
from src.monster.exceptions import AddFailedError, AddAttackFailedError, UpdateFailedError, UpdateAttackFailedError, \
    DeleteFailedError, DeleteNotFoundError


class MonsterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_name(self, name: str) -> MonsterModel | None:
        query = (select(MonsterModel)
                 .where(MonsterModel.name == name)
                 .options(selectinload(MonsterModel.abilities)))
        result = await self.session.execute(query)
        return result.scalars().first()


    async def get_all(self):
        query = (select(MonsterModel)
                 .options(selectinload(MonsterModel.abilities))
                 .order_by(MonsterModel.name))
        result = await self.session.execute(query)
        return result.scalars().all()


    async def create(self, monster_schema: MonsterInSchema):
        new_monster = MonsterModel(
            **monster_schema.model_dump(exclude={"abilities"}),
            abilities=[
                AbilityModel(**ability.model_dump())
                for ability in monster_schema.abilities
            ])
        self.session.add(new_monster)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddFailedError

        await self.session.refresh(new_monster, [
            "abilities",
        ])
        return new_monster


    async def update(self, monster_id: UUID, monster_schema: MonsterUpdateSchema) -> MonsterModel | None:
        query = (select(MonsterModel)
                 .where(MonsterModel.id == monster_id)
                 .options(selectinload(MonsterModel.abilities))
                 .with_for_update())
        result = await self.session.execute(query)
        monster = result.scalar_one_or_none()
        if monster is None:
            raise UpdateFailedError

        update_data = monster_schema.model_dump(exclude_unset=True, exclude={"abilities"})
        for field, value in update_data.items():
            setattr(monster, field, value)

        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateFailedError

        await self.session.refresh(monster, [
            "abilities",
        ])

        return monster


    async def delete(self, monster_id: UUID):
        query = (select(MonsterModel).
                 where(MonsterModel.id == monster_id).
                 with_for_update())
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
