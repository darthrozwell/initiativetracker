from uuid import UUID

from pydantic import BaseModel, ConfigDict

from src.enums_core import ConditionType
from src.action.enums import AbilityType, AbilityDistance, HitMethod, SaveEffect
from src.enums_core import DamageType


class Damage(BaseModel):
    formula: str
    type: DamageType
    hit_method: HitMethod


class AbilityEffect(BaseModel):
    distance: dict[AbilityDistance, int]
    hit_method: HitMethod
    hit_bonus: int | None = None
    dc: int | None = None
    on_successful_save: list[SaveEffect] | None = None
    damage: list[Damage] | None = None
    condition: list[ConditionType] | None = None


class ActionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: AbilityType
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
