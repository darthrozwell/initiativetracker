from typing import Union, Optional

from pydantic import BaseModel, Field, ConfigDict, create_model

from src.encounter.enums import CombatantStatus
from src.monster.schemas import MonsterInSchema


class BaseEncounter(BaseModel):
    pass

class EncounterInSchema(BaseEncounter):
    name: str
    round: int = Field(default=1, ge=0)
    current_turn: int = Field(default=0, ge=0)


class EncounterOutSchema(EncounterInSchema):
    encounter_id: str | None = None


class EncounterUpdateSchema(BaseModel):
    name: Optional[str] = None
    round: Optional[int] = Field(default=None, ge=0)
    current_turn: Optional[int] = Field(default=None, ge=0)


class CombatantInSchema(BaseModel):
    monster_id: str
    nickname: str = ""
    current_hp: int = Field(ge=0)
    current_initiative: int = Field(ge=0)
    status: CombatantStatus = CombatantStatus.ALIVE


class CombatantDbSchema(CombatantInSchema):
    model_config = ConfigDict(from_attributes=True)

    combatant_id: str
    encounter_id: str



class CombatantOutSchema(CombatantDbSchema, MonsterInSchema):
    pass


class CombatantUpdateSchema(BaseModel):
    nickname: Optional[str] = None
    current_hp: Optional[int] = Field(default=None, ge=0)
    current_initiative: Optional[int] = None
    status: Optional[CombatantStatus] = None
