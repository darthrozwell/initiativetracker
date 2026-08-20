from pydantic import BaseModel, Field, ConfigDict
from src.character.enums import Race, CharacterClass

class BaseCharacter(BaseModel):
    pass


class CharacterAttackSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = ""
    name: str = ""
    text: str = ""
    attack_type: str = ""
    attack_range: str = ""
    hit_bonus: int = 0
    reach: str = ""
    damage: str = ""

class CharacterInSchema(BaseCharacter):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(min_length=1, max_length=50)
    character_class: CharacterClass = Field(default=CharacterClass.FIGHTER)
    race: Race = Field(default=Race.HUMAN)


    armor_class: int = Field(ge=1, le=50)  # "Класс Защиты": "16",
    initiative: int = Field(le=50)  # "Инициатива": "+3 (13)",
    speed: str = Field(min_length=1, max_length=256)  # "Скорость": "20 футов, Полёта 50 футов",
    hit_points_value: int = Field(ge=1)  # "Хиты": "66 (12к8 + 12)",
    damage_resistance: str | None = None  # Сопротивление урону
    damage_immunity: str | None = None  # Иммунитеты
    damage_vulnerability: str | None = None

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

    abilities: list[CharacterAttackSchema] | None = None


class CharacterDbSchema(CharacterInSchema):
    character_id: str = Field(min_length=1, max_length=500)


class CharacterOutSchema(CharacterDbSchema):
    pass


class CharacterUpdateSchema(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    character_class: CharacterClass | None = Field(default=None)
    race: Race | None = Field(default=None)

    armor_class: int | None = Field(default=None, ge=1, le=50)  # "Класс Защиты": "16",
    initiative: int | None = Field(default=None,le=50)  # "Инициатива": "+3 (13)",
    speed: str | None = Field(default=None, min_length=1, max_length=256)  # "Скорость": "20 футов, Полёта 50 футов",
    hit_points_value: int | None = Field(default=None, ge=1)  # "Хиты": "66 (12к8 + 12)",
    damage_resistance: str | None = None  # Сопротивление урону
    damage_immunity: str | None = None  # Иммунитеты
    damage_vulnerability: str | None = None

    strength_value: int | None = Field(default=None, ge=1)
    strength_mod: int | None = Field(default=None, ge=-5)
    strength_save: int | None = Field(default=None, ge=-5)
    dexterity_value: int | None = Field(default=None, ge=1)
    dexterity_mod: int | None = Field(default=None, ge=-5)
    dexterity_save: int | None = Field(default=None, ge=-5)
    constitution_value: int | None = Field(default=None, ge=1)
    constitution_mod: int | None = Field(default=None, ge=-5)
    constitution_save: int | None = Field(default=None, ge=-5)
    intelligence_value: int | None = Field(default=None, ge=1)
    intelligence_mod: int | None = Field(default=None, ge=-5)
    intelligence_save: int | None = Field(default=None, ge=-5)
    wisdom_value: int | None = Field(default=None, ge=1)
    wisdom_mod: int | None = Field(default=None, ge=-5)
    wisdom_save: int | None = Field(default=None, ge=-5)
    charisma_value: int | None = Field(default=None, ge=1)
    charisma_mod: int | None = Field(default=None, ge=-5)
    charisma_save: int | None = Field(default=None, ge=-5)

    abilities: list[CharacterAttackSchema] | None = None
