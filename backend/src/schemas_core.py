from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from src.enums_core import CreatureAlignment


class TimestampMixinSchema(BaseModel):
    created_at: datetime
    updated_at: datetime


class CreatureMixinSchema(BaseModel):
    alignment: CreatureAlignment

    armor_class: int = Field(ge=1, le=50)  # "Класс Защиты": "16",
    initiative: int = Field(le=50)  # "Инициатива": "+3 (13)",
    speed: str = Field(min_length=1, max_length=256)  # "Скорость": "20 футов, Полёта 50 футов",
    hit_points_value: int = Field(ge=1)  # "Хиты": "66 (12к8 + 12)",
    damage_resistance: str  # Сопротивление урону
    damage_immunity: str  # Иммунитеты
    damage_vulnerability: str
    skills: str
    senses: str
    languages: str
    proficiency_bonus: int = Field(ge=1)

    strength_value: int = Field(ge=1)
    is_strength_save: bool = False
    dexterity_value: int = Field(ge=1)
    is_dexterity_save: bool = False
    constitution_value: int = Field(ge=1)
    is_constitution_save: bool = False
    intelligence_value: int = Field(ge=1)
    is_intelligence_save: bool = False
    wisdom_value: int = Field(ge=1)
    is_wisdom_save: bool = False
    charisma_value: int = Field(ge=1)
    is_charisma_save: bool = False


class CreatureUpdateMixinSchema(BaseModel):
    alignment: CreatureAlignment | None = None

    armor_class: int | None  = Field(ge=1, le=50, default=None)  # "Класс Защиты": "16",
    initiative: int | None  = Field(le=50, default=None)  # "Инициатива": "+3 (13)",
    speed: str | None  = Field(min_length=1, max_length=256, default=None)  # "Скорость": "20 футов, Полёта 50 футов",
    hit_points_value: int | None  = Field(ge=1, default=None)  # "Хиты": "66 (12к8 + 12)",
    damage_resistance: str | None = None  # Сопротивление урону
    damage_immunity: str | None = None  # Иммунитеты
    damage_vulnerability: str | None = None
    skills: str | None = None
    senses: str | None = None
    languages: str | None = None
    proficiency_bonus: int | None  = Field(ge=1, default=None)

    strength_value: int | None  = Field(ge=1, default=None)
    is_strength_save: bool | None  = None
    dexterity_value: int | None  = Field(ge=1, default=None)
    is_dexterity_save: bool | None  = None
    constitution_value: int | None  = Field(ge=1, default=None)
    is_constitution_save: bool | None  = None
    intelligence_value: int | None  = Field(ge=1, default=None)
    is_intelligence_save: bool | None  = None
    wisdom_value: int | None  = Field(ge=1, default=None)
    is_wisdom_save: bool | None  = None
    charisma_value: int | None  = Field(ge=1, default=None)
    is_charisma_save: bool | None  = None
