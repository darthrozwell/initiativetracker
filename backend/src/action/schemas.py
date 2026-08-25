from pydantic import BaseModel, ConfigDict

from src.action.enums import ActionType, DamageType


class ActionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: ActionType
    name: str
    text: str
    range: str
    reach: str
    hit_bonus: int
    damage: str
    damage_type: DamageType


class ActionDbSchema(ActionSchema):
    action_id:str


class ActionOutSchema(ActionDbSchema):
    pass


class ActionUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    action_id: str
    type: ActionType | None = None
    name: str | None = None
    text: str | None = None
    range: str | None = None
    reach: str | None = None
    hit_bonus: int | None = None
    damage: str | None = None
    damage_type: DamageType | None = None
