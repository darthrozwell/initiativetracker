from pydantic import BaseModel, Field, ConfigDict

from src.monster.enums import MonsterType, MonsterSize, MonsterSource
from src.enums_core import CreatureAlignment


class BaseMonster(BaseModel):
    pass


class MonsterAttackSchema(BaseMonster):
    model_config = ConfigDict(from_attributes=True)

    title: str = ""
    name: str = ""
    text: str = ""
    attack_type: str = ""
    attack_range: str = ""
    hit_bonus: int = 0
    reach: str = ""
    damage: str = ""

class MonsterInSchema(BaseMonster):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(min_length=1, max_length=500)
    source: MonsterSource = MonsterSource.CUSTOM
    size: MonsterSize = MonsterSize.AVG
    creature_type: MonsterType = MonsterType.HUMANOID
    alignment: CreatureAlignment = CreatureAlignment.NEUTRAL

    armor_class: int = Field(ge=1, le=50)  #"Класс Защиты": "16",
    initiative: int = Field(le=50)  #"Инициатива": "+3 (13)",
    hit_points_value: int = Field(ge=1)  #"Хиты": "66 (12к8 + 12)",
    hit_points_formula: str = Field(min_length=1, max_length=20)
    speed: str = Field(min_length=1, max_length=256)  #"Скорость": "20 футов, Полёта 50 футов",
    skills: str | None = None  #"Навыки": "Восприятие +7, Природа +5, Тайная магия +3",
    damage_resistance: str | None = None  #Сопротивление урону
    damage_immunity: str | None = None #Иммунитеты
    damage_vulnerability: str | None = None
    senses: str | None = None  #"Чувства": "пассивное Восприятие 17",
    languages: str | None = None  #"Языки": "Первичный (Ауран), Язык Ааракокра",
    challenge_rating: str = Field(min_length=1, max_length=20)
    experience: int = Field(ge=0, default=1)
    proficiency_bonus: int = Field(ge=1, default=1)
    equipment: str | None = None
    treasure: str | None = None
    habitat: str | None = None  #"Среда обитания": "Горы, Стихийный план Воздуха",

    strength_value: int = Field(ge=1, default=10)
    strength_mod: int = Field(ge=-5, default=0)
    strength_save: int = Field(ge=-5, default=0)
    dexterity_value: int = Field(ge=1, default=10)
    dexterity_mod: int = Field(ge=-5, default=0)
    dexterity_save: int = Field(ge=-5, default=0)
    constitution_value: int = Field(ge=1, default=10)
    constitution_mod: int = Field(ge=-5, default=0)
    constitution_save: int = Field(ge=-5, default=0)
    intelligence_value: int = Field(ge=1, default=10)
    intelligence_mod: int = Field(ge=-5, default=0)
    intelligence_save: int = Field(ge=-5, default=0)
    wisdom_value: int = Field(ge=1, default=10)
    wisdom_mod: int = Field(ge=-5, default=0)
    wisdom_save: int = Field(ge=-5, default=0)
    charisma_value: int = Field(ge=1, default=10)
    charisma_mod: int = Field(ge=-5, default=0)
    charisma_save: int = Field(ge=-5, default=0)

    abilities: list[MonsterAttackSchema] | None = None


class MonsterOutSchema(MonsterInSchema):
    monster_id: str = Field(min_length=1, max_length=500)



