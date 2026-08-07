from pydantic import BaseModel


class BaseEncounter(BaseModel):
    pass

class EncounterUpdateSchema(BaseEncounter):
    name: str

    round: int = 1
    current_turn: int = 0
    combatants: list | None = []
    history: list | None = []
    settings: dict | None = {}


class EncounterSchema(EncounterUpdateSchema):

    id: str | None = None


class CombatantSchema(BaseModel):
    id: str
    encounter_id: str
    monster_id: str

    nickname: str = ""
    current_hp: int = 0
    status: str = ""
