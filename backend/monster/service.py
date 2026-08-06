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

        # TEMPORARY SAVED FOR INITIAL DB FILLING
        # if "Класс Защиты" in monster_schema.info.keys(): monster_schema.armor_class = monster_schema.info["Класс Защиты"] #: str | None = None  # "Класс Защиты": "16",
        # if "Инициатива" in monster_schema.info.keys(): monster_schema.initiative = monster_schema.info["Инициатива"] # : str | None = None  # "Инициатива": "+3 (13)",
        # if "Хиты" in monster_schema.info.keys(): monster_schema.hp = monster_schema.info["Хиты"] # : str | None = None  # "Хиты": "66 (12к8 + 12)",
        # if "Скорость" in monster_schema.info.keys(): monster_schema.movement = monster_schema.info["Скорость"] # : str | None = None  # "Скорость": "20 футов, Полёта 50 футов",
        # if "Навыки" in monster_schema.info.keys(): monster_schema.skills = monster_schema.info["Навыки"] # : str | None = None  # "Навыки": "Восприятие +7, Природа +5, Тайная магия +3",
        # if "Сопротивление урону" in monster_schema.info.keys(): monster_schema.resistances = monster_schema.info['Сопротивление урону'] # : str | None = None  # Сопротивление урону
        # if "Иммунитеты" in monster_schema.info.keys(): monster_schema.immunities = monster_schema.info['Иммунитеты'] # : str | None = None  # Иммунитеты
        # if "Чувства" in monster_schema.info.keys(): monster_schema.senses = monster_schema.info["Чувства"] # : str | None = None  # "Чувства": "пассивное Восприятие 17",
        # if "Языки" in monster_schema.info.keys(): monster_schema.languages = monster_schema.info["Языки"] # : str | None = None  # "Языки": "Первичный (Ауран), Язык Ааракокра",
        # if "Среда обитания" in monster_schema.info.keys(): monster_schema.areal = monster_schema.info["Среда обитания"] # : str | None = None  # "Среда обитания": "Горы, Стихийный план Воздуха",
        # if "Снаряжение" in monster_schema.info.keys(): monster_schema.gear = monster_schema.info['Снаряжение'] # : str | None = None  # Снаряжение
        # if "Сокровища" in monster_schema.info.keys(): monster_schema.loot = monster_schema.info["Сокровища"] # : str | None = None  # "Сокровища": "Личные , Инструментальные",
        # if "Опасность" in monster_schema.info.keys(): monster_schema.danger = monster_schema.info["Опасность"] # : str | None = None  # "Опасность": "4 (1 100 опыта; БВ +2)"
        # monster_schema.strength = monster_schema.stats["СИЛ"]['value']
        # monster_schema.strength_save = monster_schema.stats["СИЛ"]['save']
        # monster_schema.dexterity = monster_schema.stats['ЛОВ']['value']
        # monster_schema.dexterity_save = monster_schema.stats['ЛОВ']['save']
        # monster_schema.intelligence = monster_schema.stats['ИНТ']['value']
        # monster_schema.intelligence_save = monster_schema.stats['ИНТ']['save']
        # monster_schema.wisdom = monster_schema.stats['МДР']['value']
        # monster_schema.wisdom_save = monster_schema.stats['МДР']['save']
        # monster_schema.charisma = monster_schema.stats['ХАР']['value']
        # monster_schema.charisma_save = monster_schema.stats['ХАР']['save']
        # monster_schema.constitution = monster_schema.stats['ТЕЛ']['value']
        # monster_schema.constitution_save = monster_schema.stats['ТЕЛ']['save']
