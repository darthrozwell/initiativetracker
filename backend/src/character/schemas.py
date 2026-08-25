from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict

from src.damage.schemas import DamageProtectionSchema
from src.action.schemas import ActionSchema, ActionDbSchema, ActionOutSchema, ActionUpdateSchema
from src.schemas_core import CreatureMixinSchema, CreatureUpdateMixinSchema, TimestampMixinSchema
from src.character.enums import Race, CharacterClass


class CharacterInSchema(CreatureMixinSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(min_length=1, max_length=50)
    character_class: CharacterClass
    race: Race

    actions: list[ActionSchema]
    protections: DamageProtectionSchema


class CharacterDbSchema(CharacterInSchema, TimestampMixinSchema):
    character_id: UUID
    actions: list[ActionDbSchema]


class CharacterOutSchema(CharacterDbSchema):
    actions: list[ActionOutSchema]


class CharacterUpdateSchema(CreatureUpdateMixinSchema, BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    character_class: CharacterClass | None = None
    race: Race | None = None

    actions: list[ActionUpdateSchema] | None = None
    protections: DamageProtectionSchema | None = None
