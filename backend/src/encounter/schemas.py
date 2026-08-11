from pydantic import BaseModel, Field, ConfigDict

from src.encounter.enums import CombatantStatus
from src.monster.schemas import MonsterInSchema


class BaseEncounter(BaseModel):
    pass

class EncounterInSchema(BaseEncounter):
    name: str
    round: int = 1
    current_turn: int = 0


class EncounterOutSchema(EncounterInSchema):
    encounter_id: str | None = None


class CombatantInSchema(BaseModel):
    monster_id: str
    nickname: str = ""
    current_hp: int = Field(ge=0)
    status: CombatantStatus = CombatantStatus.UNCONSCIOUS.ALIVE

class CombatantDbSchema(CombatantInSchema):
    model_config = ConfigDict(from_attributes=True)

    combatant_id: str
    encounter_id: str


class CombatantOutSchema(CombatantDbSchema, MonsterInSchema):
    pass
