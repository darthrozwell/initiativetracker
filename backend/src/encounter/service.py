import uuid
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.encounter.exceptions import AddEncFailedError, DeleteEncNotFoundError, DeleteEncFailedError, UpdateEncFailedError, \
    AddCombFailedError, UpdateCombFailedError, DeleteCombFailedError, DeleteCombNotFoundError
from src.monster.schemas import MonsterInSchema
from src.encounter.models import EncounterModel, CombatantModel
from src.encounter.schemas import EncounterInSchema, CombatantInSchema, CombatantDbSchema
from src.monster.models import MonsterModel


class EncounterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_encounter(self, name: str) -> EncounterModel | None:
        query = select(EncounterModel).where(EncounterModel.encounter_id == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def get_all_encounters(self):
        query = select(EncounterModel).order_by(EncounterModel.name)
        result = await self.session.execute(query)
        return result.scalars().all()


    async def create_encounter(self, new_schema: EncounterInSchema) -> EncounterModel | None:
        new_model = EncounterModel(**new_schema.model_dump())
        new_model.encounter_id = str(uuid.uuid4())
        self.session.add(new_model)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddEncFailedError
        return new_model


    async def delete_encounter(self, encounter_id: str):
        query = select(EncounterModel).where(EncounterModel.encounter_id == encounter_id).with_for_update()
        result = await self.session.execute(query)
        res = result.scalar_one_or_none()
        if res is None:
            raise DeleteEncNotFoundError
        try:
            await self.session.delete(res)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise DeleteEncFailedError
        return


    async def update_encounter(self, encounter_id: str, encounter: EncounterInSchema) -> EncounterModel | None:
        query = update(EncounterModel).where(EncounterModel.encounter_id == encounter_id).values(**encounter.model_dump())
        result = await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateEncFailedError
        return


    async def get_combatants(self, encounter_id: str):
        query = (select(CombatantModel, MonsterModel).
                 join(MonsterModel, CombatantModel.monster_id == MonsterModel.monster_id).
                 where(CombatantModel.encounter_id == encounter_id))

        result = await self.session.execute(query)
        combatants = []
        for combatant, monster in result:
            combatants.append(
                {
                    **CombatantDbSchema.model_validate(combatant, extra= 'ignore').model_dump(),
                    **MonsterInSchema.model_validate(monster, extra= 'ignore').model_dump()
                 }
            )
        return combatants


    async def create_combatant(self, encounter_id: str, combatant_in: CombatantInSchema):
        new_model = CombatantModel(**combatant_in.model_dump())
        new_model.combatant_id = str(uuid.uuid4())
        new_model.encounter_id = encounter_id
        self.session.add(new_model)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddCombFailedError
        query = select(MonsterModel).where(MonsterModel.monster_id == combatant_in.monster_id)
        result = await self.session.execute(query)
        monster = result.scalar_one_or_none()
        combatant = {
            **CombatantDbSchema.model_validate(new_model, extra='ignore').model_dump(),
            **MonsterInSchema.model_validate(monster, extra='ignore').model_dump(),
        }
        return combatant


    async def update_combatant(self, combatant_id: str, new_schema: CombatantInSchema):
        query = update(CombatantModel).where(CombatantModel.combatant_id == combatant_id).values(**new_schema.model_dump())
        await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateCombFailedError
        return

    async def delete_combatant(self, combatant_id: str):
        query = select(CombatantModel).where(CombatantModel.combatant_id == combatant_id)
        result = await self.session.execute(query)
        res = result.scalar_one_or_none()
        if res is None:
            raise DeleteCombNotFoundError
        try:
            await self.session.delete(res)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise DeleteCombFailedError
        return
