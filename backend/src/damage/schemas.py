from pydantic import BaseModel, ConfigDict

from src.enums_core import DamageType, ConditionType


class DamageProtectionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    damage_resistance: list[DamageType]
    damage_vulnerability: list[DamageType]
    damage_immunity: list[DamageType | ConditionType]
