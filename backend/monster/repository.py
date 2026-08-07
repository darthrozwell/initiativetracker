import uuid

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from monster.models import MonsterModel, MonsterAttackModel
from monster.schemas import MonsterSchema


class MonsterRepo:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_name(self, name: str) -> MonsterModel | None:
        query = select(MonsterModel).where(MonsterModel.name == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def get_all(self):
        query = select(MonsterModel).order_by(MonsterModel.name)
        result = await self.session.execute(query)
        return result.scalars()


    async def add(self, monster_schema: MonsterSchema):
        new_monster = MonsterModel(**monster_schema.model_dump(exclude={"abilities"}))
        new_monster.id = str(uuid.uuid4())
        self.session.add(new_monster)
        await self.session.commit()
        if monster_schema.abilities is not None:
            for data_abilities in monster_schema.abilities:
                new_ability = MonsterAttackModel(**data_abilities.model_dump())
                new_ability.id = str(uuid.uuid4())
                new_ability.monster_name = new_monster.name
                self.session.add(new_ability)
        await self.session.commit()


    async def update(self, monster_schema: MonsterSchema):
        data = monster_schema.model_dump(exclude={"abilities"})
        query = update(MonsterModel).where(MonsterModel.id == monster_schema.id).values(**data)
        result = await self.session.execute(query)
        await self.session.commit()
        if monster_schema.abilities is not None:
            for data_abilities in monster_schema.abilities:
                query = update(MonsterAttackModel).where(MonsterAttackModel.monster_name == monster_schema.name).values(**data_abilities.model_dump())
                result = await self.session.execute(query)
        await self.session.commit()


    async def delete(self, monster_id: str):
        query = select(MonsterModel).where(MonsterModel.id == monster_id).with_for_update()
        result = await self.session.execute(query)
        res = result.scalar_one_or_none()
        if res:
            await self.session.delete(res)
        await self.session.commit()
