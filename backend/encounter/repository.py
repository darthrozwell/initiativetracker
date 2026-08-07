import uuid

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from encounter.models import EncounterModel, CombatantModel
from encounter.schemas import EncounterSchema, EncounterUpdateSchema, CombatantSchema


class EncounterRepo:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_id(self, name: str) -> EncounterModel | None:
        query = select(EncounterModel).where(EncounterModel.id == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def get_all(self):
        query = select(EncounterModel).order_by(EncounterModel.name)
        result = await self.session.execute(query)
        return result.scalars() #.scalars()


    async def create(self, new_schema: EncounterSchema) -> EncounterModel | None:
        new_model = EncounterModel(**new_schema.model_dump())
        new_model.id = str(uuid.uuid4())
        self.session.add(new_model)
        await self.session.commit()
        return new_model


    async def delete(self, encounter_id: str):
        query = select(EncounterModel).where(EncounterModel.id == encounter_id).with_for_update()
        result = await self.session.execute(query)
        res = result.scalar_one_or_none()
        if res:
            await self.session.delete(res)
        await self.session.commit()
        return


    async def update(self, encounter_id: str, new_schema: EncounterUpdateSchema) -> EncounterModel | None:
        query = update(EncounterModel).where(EncounterModel.id == encounter_id).values(**new_schema.model_dump())
        result = await self.session.execute(query)
        await self.session.commit()
        return


    async def get_combatants(self, encounter_id: str):
        query = select(CombatantModel).where(CombatantModel.encounter_id == encounter_id)
        result = await self.session.execute(query)
        return result.scalars()


    async def create_combatant(self, encounter_id: str, new_schema: CombatantSchema):
        new_model = CombatantModel(**new_schema.model_dump())
        new_model.id = str(uuid.uuid4())
        self.session.add(new_model)
        await self.session.commit()
        return new_model


    async def update_combatant(self, new_schema: CombatantSchema):
        query = update(CombatantModel).where(CombatantModel.id == new_schema.id).values(**new_schema.model_dump())
        result = await self.session.execute(query)
        await self.session.commit()
        return

    async def delete_combatant(self, combatant_id: str):
        query = delete(CombatantModel).where(CombatantModel.id == combatant_id)
        await self.session.execute(query)
        await self.session.commit()
        return
