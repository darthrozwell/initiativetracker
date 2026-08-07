from pydantic import BaseModel, Field
from typing_extensions import Any


class BaseMonster(BaseModel):
    pass

class MonsterSchema(BaseMonster):
    id: str | None = None
    name: str = Field(min_length=1, max_length=500)
    source: str | None = Field(min_length=1, max_length=500)
    size: str | None = Field(min_length=1, max_length=500)
    creature_type: str | None = Field(min_length=1, max_length=500)
    alignment: str | None = Field(min_length=1, max_length=500)

    armor_class: int = 0 #"Класс Защиты": "16",
    initiative: int = 0  #"Инициатива": "+3 (13)",
    hit_points_value: int = 0  #"Хиты": "66 (12к8 + 12)",
    hit_points_formula: str = ""
    speed: str = ""  #"Скорость": "20 футов, Полёта 50 футов",
    skills: str | None = None  #"Навыки": "Восприятие +7, Природа +5, Тайная магия +3",
    damage_resistance: str | None = None  #Сопротивление урону
    damage_immunity: str | None = None #Иммунитеты
    damage_vulnerability: str | None = None
    senses: str | None = None  #"Чувства": "пассивное Восприятие 17",
    languages: str | None = None  #"Языки": "Первичный (Ауран), Язык Ааракокра",
    challenge_rating: str = "0"
    experience: int = 0
    proficiency_bonus: int = 0
    equipment: str | None = None
    treasure: str | None = None
    habitat: str | None = None  #"Среда обитания": "Горы, Стихийный план Воздуха",

    strength_value: int = 0
    strength_mod: int = -5
    strength_save: int = -5
    dexterity_value: int = 0
    dexterity_mod: int = -5
    dexterity_save: int = -5
    constitution_value: int = 0
    constitution_mod: int = -5
    constitution_save: int = -5
    intelligence_value: int = 0
    intelligence_mod: int = -5
    intelligence_save: int = -5
    wisdom_value: int = 0
    wisdom_mod: int = -5
    wisdom_save: int = -5
    charisma_value: int = 0
    charisma_mod: int = -5
    charisma_save: int = -5

    abilities: list[MonsterAttackSchema] | None = None


class MonsterAttackSchema(BaseMonster):
    title: str = ""
    name: str = ""
    text: str = ""
    attack_type: str = ""
    attack_range: str = ""
    hit_bonus: int = 0
    reach: str = ""
    damage: str = ""
