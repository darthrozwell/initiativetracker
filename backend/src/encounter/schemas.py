from pydantic import BaseModel, Field, ConfigDict

from src.character.schemas import CharacterOutSchema
from src.encounter.enums import CombatantStatus
from src.monster.schemas import MonsterOutSchema


class EncounterInSchema(BaseModel):
    name: str
    round: int = Field(default=1, ge=0)
    current_turn: int = Field(default=0, ge=0)


class EncounterOutSchema(EncounterInSchema):
    encounter_id: str | None = None


class EncounterUpdateSchema(BaseModel):
    name: str | None = None
    round: int | None = Field(default=None, ge=0)
    current_turn: int | None = Field(default=None, ge=0)


class CombatantInSchema(BaseModel):
    monster_id: str | None = None
    character_id: str | None = None
    nickname: str
    current_hp: int = Field(ge=0)
    current_initiative: int = Field(ge=0)
    status: CombatantStatus


class CombatantDbSchema(CombatantInSchema):
    model_config = ConfigDict(from_attributes=True)

    combatant_id: str
    encounter_id: str


class CombatantOutMonsterSchema(CombatantDbSchema, MonsterOutSchema):
    pass


class CombatantOutCharacterSchema(CombatantDbSchema, CharacterOutSchema):
    pass


class CombatantUpdateSchema(BaseModel):
    nickname: str | None = None
    current_hp: int | None = Field(default=None, ge=0)
    current_initiative: int | None = Field(default=None, ge=0)
    status: CombatantStatus | None = None
