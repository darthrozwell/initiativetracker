import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from monster.models import MonsterModel


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
        return result

    async def add_monster(self, monster: MonsterModel):
        monster.id = str(uuid.uuid4())
        self.session.add(monster)
        await self.session.commit()

    async def delete(self, monster_id: str):
        query = select(MonsterModel).where(MonsterModel.id == monster_id)
        result = await self.session.execute(query)
        res = result.scalar_one_or_none()
        if res:
            await self.session.delete(res)
        await self.session.commit()
