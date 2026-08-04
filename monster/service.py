from monster.repository import MonsterRepo
from monster.models import MonsterModel


class MonsterService:
    def __init__(self, repository: MonsterRepo):
        self.repository = repository

    async def get_by_name(self, name) -> MonsterModel | None:
        return await self.repository.get_by_name(name)

    async def get_all(self) -> list[MonsterModel]:
        return await self.repository.get_all()

    async def add_monster(self, name: str) -> None:
        await self.repository.add_monster(name=name)

