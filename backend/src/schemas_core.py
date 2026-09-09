from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field

from src.enums_core import CreatureAlignment, ConditionType, CreatureSize, CreatureSource, DamageType, Skills


class TimestampMixinSchema(BaseModel):
    created_at: datetime
    updated_at: datetime


class CreatureMixinSchema(BaseModel):
    armor_class: int = Field(ge=1)
    initiative: int = Field(ge=0)
    hit_points: int = Field(ge=1)
    hit_points_formula: str = Field(min_length=1, examples=["1d6 + 2"])
    speed: dict[str, int] = Field(default_factory=dict, examples=[{"walk": 30, "fly": 50}])

    resistances: list[DamageType] = Field(default_factory=list)
    immunities: list[DamageType] = Field(default_factory=list)
    vulnerabilities: list[DamageType] = Field(default_factory=list)
    condition_immunities: list[ConditionType] = Field(default_factory=list)

    strength: int = Field(ge=1)
    dexterity: int = Field(ge=1)
    constitution: int = Field(ge=1)
    intelligence: int = Field(ge=1)
    wisdom: int = Field(ge=1)
    charisma: int = Field(ge=1)
    saves: dict[str, str] = Field(default_factory=dict, examples=[{"str": "-2", "wis": "+4"}])

    name: str = Field(min_length=1, max_length=500, examples=["BFMonster"])
    alignment: CreatureAlignment
    size: CreatureSize
    source: CreatureSource

    skills: dict[Skills, str] = Field(default_factory=dict, examples=[{"acrobatics": "+5", "athletics": "+10"}])
    senses: list[str] = Field(default_factory=list, examples=[["Darkvision 60 ft."], ["Truesight 120 ft."]])
    languages: list[str] = Field(default_factory=list, examples=[["Common"], ["Deep Speech", "Undercommon; telepathy 120 ft."]])


class CreatureUpdateMixinSchema(BaseModel):
    id: UUID

    armor_class: int | None = Field(ge=1, default=None)
    initiative: int | None = Field(ge=0, default=None)
    hit_points: int | None = Field(ge=1, default=None)
    hit_points_formula: str | None = None
    speed: dict[str, int] | None = None

    resistances: list[DamageType] | None = None
    immunities: list[DamageType] | None = None
    vulnerabilities: list[DamageType] | None = None
    condition_immunities: list[ConditionType] | None = None

    strength: int | None = Field(ge=1, default=None)
    dexterity: int | None= Field(ge=1, default=None)
    constitution: int | None = Field(ge=1, default=None)
    intelligence: int | None = Field(ge=1, default=None)
    wisdom: int | None = Field(ge=1, default=None)
    charisma: int | None = Field(ge=1, default=None)
    saves: dict[str, str] | None = None

    name: str | None = Field(min_length=1, max_length=500, default=None)
    alignment: CreatureAlignment | None = None
    size: CreatureSize | None = None
    source: CreatureSource | None = None

    skills: dict[Skills, str] | None = None
    senses: list[str] | None = None
    languages: list[str] | None = None
