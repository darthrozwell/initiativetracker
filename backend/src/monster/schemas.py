from pydantic import BaseModel, Field, ConfigDict

from src.monster.enums import MonsterType, MonsterSize, MonsterSource
from src.action.schemas import ActionSchema, ActionUpdateSchema, ActionDbSchema, ActionOutSchema
from src.schemas_core import CreatureMixinSchema, CreatureUpdateMixinSchema, TimestampMixinSchema


class MonsterInSchema(CreatureMixinSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(min_length=1, max_length=500)
    source: MonsterSource
    size: MonsterSize
    creature_type: MonsterType

    hit_points_formula: str = Field(min_length=1, max_length=20)
    challenge_rating: str = Field(min_length=1, max_length=20)
    experience: int = Field(ge=0, default=1)
    equipment: str
    treasure: str
    habitat: str

    actions: list[ActionSchema]


class MonsterDbSchema(MonsterInSchema, TimestampMixinSchema):
    model_config = ConfigDict(from_attributes=True)

    monster_id: str
    actions: list[ActionDbSchema]


class MonsterOutSchema(MonsterDbSchema):
    actions: list[ActionOutSchema]


class MonsterUpdateSchema(CreatureUpdateMixinSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str | None = None
    source: MonsterSource | None = None
    size: MonsterSize | None = None
    creature_type: MonsterType | None = None

    hit_points_formula: str | None = Field(min_length=1, max_length=20, default=None)
    challenge_rating: str | None = Field(min_length=1, max_length=20, default=None)
    experience: int | None = Field(ge=0, default=None)
    equipment: str | None = None
    treasure: str | None = None
    habitat: str | None = None

    actions: list[ActionUpdateSchema] | None = None
