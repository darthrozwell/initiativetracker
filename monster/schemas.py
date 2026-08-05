from collections import defaultdict

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class BaseMonster(BaseModel):
    pass

class MonsterSchema(BaseMonster):
    id: str | None = None
    name: str = Field(min_length=1, max_length=500)
    source: str | None = Field(min_length=1, max_length=500)
    size: str | None = Field(min_length=1, max_length=500)
    creature_type: str | None = Field(min_length=1, max_length=500)
    alignment: str | None = Field(min_length=1, max_length=500)
    info: dict | None = None
    abilities: list | None = None
    stats: dict | None = None

    armor_class: str | None = None #"Класс Защиты": "16",
    initiative: str | None = None  #"Инициатива": "+3 (13)",
    hp: str | None = None  #"Хиты": "66 (12к8 + 12)",
    movement: str | None = None  #"Скорость": "20 футов, Полёта 50 футов",
    skills: str | None = None  #"Навыки": "Восприятие +7, Природа +5, Тайная магия +3",
    resistances: str | None = None  #Сопротивление урону
    immunities: str | None = None #Иммунитеты
    senses: str | None = None  #"Чувства": "пассивное Восприятие 17",
    languages: str | None = None  #"Языки": "Первичный (Ауран), Язык Ааракокра",
    areal: str | None = None  #"Среда обитания": "Горы, Стихийный план Воздуха",
    gear: str | None = None  #Снаряжение
    loot: str | None = None #"Сокровища": "Личные , Инструментальные",
    danger: str | None = None  #"Опасность": "4 (1 100 опыта; БВ +2)"

    strength: int | None = None
    dexterity: int | None = None
    constitution: int | None = None
    intelligence: int | None = None
    wisdom: int | None = None
    charisma: int | None = None
    strength_save: str | None = None
    dexterity_save: str | None = None
    constitution_save: str | None = None
    intelligence_save: str | None = None
    wisdom_save: str | None = None
    charisma_save: str | None = None

