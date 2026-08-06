from encounter.models import EncounterModel
from encounter.repository import EncounterRepo
from encounter.schemas import EncounterSchema


class EncounterService:
    def __init__(self, repository: EncounterRepo):
        self.repository = repository


    async def get_encounter(self, encounter_id: str):
        encounter = await self.repository.get_by_id(encounter_id)
        return encounter


    async def create_encounter(self) -> EncounterModel | None:
        new_schema = EncounterSchema(name="new_encounter")
        encounter = await self.repository.create(new_schema)
        return encounter
