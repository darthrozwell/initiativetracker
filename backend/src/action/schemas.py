from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.action.enums import ActionType
from src.enums_core import DamageType


class Damage(BaseModel):
    damage: str
    damage_type: DamageType


class ActionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: ActionType
    name: str
    text: str
    range: str
    reach: str
    hit_bonus: int
    damage: list[Damage]


class ActionDbSchema(ActionSchema):
    action_id: UUID

    monster_id: UUID | None = None
    character_id: UUID | None = None


class ActionOutSchema(ActionDbSchema):
    pass


class ActionUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    action_id: UUID
    type: ActionType | None = None
    name: str | None = None
    text: str | None = None
    range: str | None = None
    reach: str | None = None
    hit_bonus: int | None = None
    damage: str | None = None
    damage_type: list[Damage] | None = None
