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
