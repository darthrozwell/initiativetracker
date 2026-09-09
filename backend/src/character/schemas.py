from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict

from src.schemas_core import CreatureMixinSchema, CreatureUpdateMixinSchema, TimestampMixinSchema
from src.action.schemas import AbilityInSchema, AbilityDbSchema, AbilityOutSchema, AbilityUpdateSchema
from src.character.enums import Race, CharacterClass


class CharacterInSchema(CreatureMixinSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    character_class: CharacterClass
    race: Race
    abilities: list[AbilityInSchema]


class CharacterDbSchema(CharacterInSchema, TimestampMixinSchema):
    id: UUID

    abilities: list[AbilityDbSchema]


class CharacterOutSchema(CharacterDbSchema):
    abilities: list[AbilityOutSchema]


class CharacterUpdateSchema(CreatureUpdateMixinSchema, BaseModel):
    id : UUID

    character_class: CharacterClass | None = None
    race: Race | None = None
    abilities: list[AbilityUpdateSchema] | None = None
