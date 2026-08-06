from encounter.models import EncounterModel
from encounter.repository import EncounterRepo
from encounter.schemas import EncounterSchema, EncounterUpdateSchema


class EncounterService:
    def __init__(self, repository: EncounterRepo):
        self.repository = repository


    async def get_encounter(self, encounter_id: str):
        encounter = await self.repository.get_by_id(encounter_id)
        return encounter


    async def get_all_encounters(self):
        encounters = await self.repository.get_all()
        return encounters


    async def create_encounter(self) -> EncounterModel | None:
        new_schema = EncounterSchema(name="new_encounter")
        encounter = await self.repository.create(new_schema)
        return encounter


    async def delete_encounter(self, encounter_id: str):
        await self.repository.delete(encounter_id=encounter_id)
        return


    async def update_encounter(self, encounter_id: str, encounter: EncounterUpdateSchema):
        await self.repository.update(encounter_id=encounter_id, new_schema=encounter)
        return