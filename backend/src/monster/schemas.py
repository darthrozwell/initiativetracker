from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

from src.schemas_core import CreatureMixinSchema, CreatureUpdateMixinSchema, TimestampMixinSchema
from src.monster.enums import MonsterType
from src.action.schemas import AbilityInSchema, AbilityDbSchema, AbilityOutSchema, AbilityUpdateSchema


class MonsterInSchema(CreatureMixinSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: MonsterType
    challenge_rating: str = Field(min_length=1, max_length=20, examples=["1/4", "1/2", "2", "20"])
    equipment: list[str] = Field(default_factory=list, examples=[["spear|xphb"], ["breastplate|xphb"]])
    treasure: list[str] = Field(default_factory=list, examples=[["any"], ["armaments"]])
    environment: list[str] = Field(default_factory=list, examples=[["underdark"], ["any"], ["mountain", "planar, earth", "underdark"], ["planar, abyss"]])

    abilities: list[AbilityInSchema]


class MonsterDbSchema(MonsterInSchema, TimestampMixinSchema):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    abilities: list[AbilityDbSchema]


class MonsterOutSchema(MonsterDbSchema):
    model_config = ConfigDict(from_attributes=True)

    abilities: list[AbilityOutSchema]

class MonsterUpdateSchema(CreatureUpdateMixinSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: MonsterType | None = None
    challenge_rating: str | None = Field(min_length=1, max_length=20, default=None)
    equipment: list[str] | None = None
    treasure: list[str] | None = None
    environment: list[str] | None = None

    abilities: list[AbilityUpdateSchema] | None = None
