from pydantic import BaseModel, Field, ConfigDict

from src.action.schemas import ActionSchema, ActionDbSchema, ActionOutSchema, ActionUpdateSchema
from src.schemas_core import CreatureMixinSchema, CreatureUpdateMixinSchema
from src.character.enums import Race, CharacterClass


class CharacterInSchema(CreatureMixinSchema, BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(min_length=1, max_length=50)
    character_class: CharacterClass
    race: Race

    actions: list[ActionSchema]


class CharacterDbSchema(CharacterInSchema):
    character_id: str = Field(min_length=1, max_length=500)
    actions: list[ActionDbSchema]


class CharacterOutSchema(CharacterDbSchema):
    actions: list[ActionOutSchema]


class CharacterUpdateSchema(CreatureUpdateMixinSchema, BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    character_class: CharacterClass | None = None
    race: Race | None = None

    actions: list[ActionUpdateSchema] | None = None
