from monster.repository import MonsterRepo
from monster.models import MonsterModel
from monster.schemas import MonsterSchema


class MonsterService:
    def __init__(self, repository: MonsterRepo):
        self.repository = repository


    async def get_by_name(self, name: str) -> MonsterModel | None:
        return await self.repository.get_by_name(name)


    async def get_all_monsters(self) -> list[MonsterModel]:
        return await self.repository.get_all()


    async def update_monster(self, monster_schema: MonsterSchema):
        await self.repository.update(monster_schema=monster_schema)


    async def delete_monster(self, monster_id: str):
        return await self.repository.delete(monster_id)


    async def add_monster(self, monster_schema: MonsterSchema) -> None:
        await self.repository.add(monster_schema=monster_schema)
