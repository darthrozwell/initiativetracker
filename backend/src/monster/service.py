import uuid
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.action.models import ActionModel
from src.monster.exceptions import AddFailedError, AddAttackFailedError, UpdateFailedError, UpdateAttackFailedError, \
    DeleteFailedError, DeleteNotFoundError
from src.monster.models import MonsterModel
from src.monster.schemas import MonsterInSchema, MonsterUpdateSchema


class MonsterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_name(self, name: str) -> MonsterModel | None:
        query = (select(MonsterModel)
                 .where(MonsterModel.name == name)
                 .options(selectinload(MonsterModel.actions)))
        result = await self.session.execute(query)
        return result.scalars().first()


    async def get_all(self):
        query = (select(MonsterModel)
                 .options(selectinload(MonsterModel.actions))
                 .order_by(MonsterModel.name))
        result = await self.session.execute(query)
        return result.scalars().all()


    async def add(self, monster_schema: MonsterInSchema):
        new_monster = MonsterModel(**monster_schema.model_dump(exclude={"actions"}))
        new_monster.monster_id = str(uuid.uuid4())
        self.session.add(new_monster)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddFailedError
        if monster_schema.actions is not None:
            for action in monster_schema.actions:
                new_action = ActionModel(**action.model_dump())
                new_action.action_id = str(uuid.uuid4())
                new_action.monster_id = new_monster.monster_id
                self.session.add(new_action)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddAttackFailedError

        result = await self.session.execute(
            select(MonsterModel)
            .options(selectinload(MonsterModel.actions))
            .where(MonsterModel.monster_id == new_monster.monster_id)
        )
        new_monster = result.scalar_one()
        return new_monster


    async def update(self, monster_id: str, monster_schema: MonsterUpdateSchema):
        data = monster_schema.model_dump(exclude={"actions"}, exclude_unset=True)
        query = (update(MonsterModel)
                 .where(MonsterModel.monster_id == monster_id)
                 .values(**data))
        await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateFailedError
        if monster_schema.actions is not None:
            for action in monster_schema.actions:
                query = (update(ActionModel)
                         .where(ActionModel.action_id == action.action_id)
                         .values(**action.model_dump(exclude_unset=True)))
                result = await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateAttackFailedError
        return


    async def delete(self, monster_id: str):
        query = (select(MonsterModel).
                 where(MonsterModel.monster_id == monster_id).
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
