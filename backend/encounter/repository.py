import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from encounter.models import EncounterModel
from encounter.schemas import EncounterSchema


class EncounterRepo:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_id(self, name: str) -> EncounterModel | None:
        query = select(EncounterModel).where(EncounterModel.id == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def create(self, new_schema: EncounterSchema) -> EncounterModel | None:
        new_model = EncounterModel(**new_schema.model_dump())
        new_model.id = str(uuid.uuid4())
        self.session.add(new_model)
        await self.session.commit()
        return new_model
