from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

from src.enums_core import ConditionType, DamageType
from src.action.enums import AbilityType, AbilityDistance, HitMethod, SaveEffect


class Damage(BaseModel):
    formula: str = Field(min_length=1, examples=["1d4 + 1"])
    type: DamageType
    hit_method: HitMethod


class AbilityInSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: AbilityType
    name: str = Field(min_length=1, max_length=500, examples=["BFAbility"])
    text: str = Field(min_length=1, max_length=5000, examples=["Some text for this"])
    distance: dict[AbilityDistance, int] = Field(default_factory=dict, examples=[{"range": 20, "reach": 5}])
    hit_method: HitMethod
    hit_bonus: int | None = None
    dc: int | None = None
    on_successful_save: list[SaveEffect] | None = None
    damage: list[Damage] | None = None
    condition: list[ConditionType] | None = None


class AbilityDbSchema(AbilityInSchema):
    model_config = ConfigDict(from_attributes=True)

    id: UUID


class AbilityOutSchema(AbilityDbSchema):
    model_config = ConfigDict(from_attributes=True)


class AbilityUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    type: AbilityType | None = None
    name: str | None = Field(min_length=1, max_length=500, default=None)
    text: str | None = Field(min_length=1, max_length=5000, default=None)
    distance: dict[AbilityDistance, int] | None = None
    hit_method: HitMethod | None = None
    hit_bonus: int | None = None
    dc: int | None = None
    on_successful_save: list[SaveEffect] | None = None
    damage: list[Damage] | None = None
    condition: list[ConditionType] | None = None
