from pydantic import BaseModel


class BaseEncounter(BaseModel):
    pass


class EncounterSchema(BaseEncounter):

    id: str | None = None
    name: str

    round: int = 0
    current_turn: int = 0
    combatants: list | None = None
    history: list | None = None
    settings: dict | None = None
