from uuid import UUID
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.encounter.schemas import CombatantOutMonsterSchema
from src.character.schemas import CharacterInSchema, CharacterDbSchema
from src.character.models import CharacterModel
from src.encounter.exceptions import AddEncFailedError, DeleteEncNotFoundError, DeleteEncFailedError, \
    UpdateEncFailedError, \
    AddCombFailedError, UpdateCombFailedError, DeleteCombFailedError, DeleteCombNotFoundError, CombatantHasNoTypeError
from src.monster.schemas import MonsterInSchema, MonsterDbSchema
from src.encounter.models import EncounterModel, CombatantModel
from src.encounter.schemas import EncounterInSchema, CombatantInSchema, CombatantDbSchema, CombatantUpdateSchema, \
    EncounterUpdateSchema
from src.monster.models import MonsterModel


class EncounterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_encounter(self, encounter_id: UUID) -> EncounterModel | None:
        query = (select(EncounterModel)
                 .where(EncounterModel.encounter_id == encounter_id))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def get_all_encounters(self):
        query = (select(EncounterModel)
                 .order_by(EncounterModel.name))
        result = await self.session.execute(query)
        return result.scalars().all()


    async def create_encounter(self, new_schema: EncounterInSchema) -> EncounterModel | None:
        new_model = EncounterModel(**new_schema.model_dump())
        self.session.add(new_model)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddEncFailedError
        return new_model


    async def delete_encounter(self, encounter_id: UUID):
        query = (select(EncounterModel)
                 .where(EncounterModel.encounter_id == encounter_id)
                 .with_for_update())
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


    async def update_encounter(self, encounter_id: UUID, encounter_schema: EncounterUpdateSchema) -> None:
        query = (select(EncounterModel)
                 .where(EncounterModel.encounter_id == encounter_id)
                 .with_for_update())
        result = await self.session.execute(query)
        encounter = result.scalar_one_or_none()
        if encounter is None:
            raise UpdateEncFailedError

        update_data = encounter_schema.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(encounter, field, value)

        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateEncFailedError
        return


    async def get_combatants(self, encounter_id: UUID):
        query = (select(CombatantModel, MonsterModel, CharacterModel).
                 outerjoin(MonsterModel, CombatantModel.monster_id == MonsterModel.monster_id).
                 outerjoin(CharacterModel, CombatantModel.character_id == CharacterModel.character_id).
                 options(selectinload(MonsterModel.actions),
                         selectinload(MonsterModel.damage_vulnerability),
                         selectinload(MonsterModel.damage_resistance),
                         selectinload(MonsterModel.damage_immunity),
                         selectinload(CharacterModel.actions),
                         selectinload(CharacterModel.damage_vulnerability),
                         selectinload(CharacterModel.damage_resistance),
                         selectinload(CharacterModel.damage_immunity),).
                 where(CombatantModel.encounter_id == encounter_id))

        result = await self.session.execute(query)
        combatants = []
        for combatant, monster, character in result:
            if combatant.monster_id is not None:
                combatants.append(
                    {
                        **CombatantDbSchema.model_validate(combatant, extra= 'ignore').model_dump(),
                        **MonsterDbSchema.model_validate(monster, extra= 'ignore').model_dump()
                     }
                )
            elif combatant.character_id is not None:
                combatants.append(
                    {
                        **CombatantDbSchema.model_validate(combatant, extra='ignore').model_dump(),
                        **CharacterDbSchema.model_validate(character, extra='ignore').model_dump()
                    }
                )
            else:
                raise CombatantHasNoTypeError
        return combatants


    async def create_combatant(self, encounter_id: UUID, combatant_in: CombatantInSchema):
        new_model = CombatantModel(**combatant_in.model_dump())
        new_model.encounter_id = encounter_id
        self.session.add(new_model)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddCombFailedError
        if combatant_in.monster_id is not None:
            query = (select(MonsterModel)
                     .options(selectinload(MonsterModel.actions),
                         selectinload(MonsterModel.damage_vulnerability),
                         selectinload(MonsterModel.damage_resistance),
                         selectinload(MonsterModel.damage_immunity),)
                     .where(MonsterModel.monster_id == combatant_in.monster_id))
            result = await self.session.execute(query)
            monster = result.scalar_one_or_none()
            combatant = {
                **CombatantDbSchema.model_validate(new_model, extra='ignore').model_dump(),
                **MonsterDbSchema.model_validate(monster, extra='ignore').model_dump(),
            }
        elif combatant_in.character_id is not None:
            query = (select(CharacterModel)
                     .options(selectinload(CharacterModel.actions),
                         selectinload(CharacterModel.damage_vulnerability),
                         selectinload(CharacterModel.damage_resistance),
                         selectinload(CharacterModel.damage_immunity),)
                     .where(CharacterModel.character_id == combatant_in.character_id))
            result = await self.session.execute(query)
            character = result.scalar_one_or_none()
            combatant = {
                **CombatantDbSchema.model_validate(new_model, extra='ignore').model_dump(),
                **CharacterDbSchema.model_validate(character, extra='ignore').model_dump(),
            }
        else:
            raise CombatantHasNoTypeError
        return combatant


    async def update_combatant(self, combatant_id: UUID, new_schema: CombatantUpdateSchema):
        query = (select(CombatantModel)
                 .where(CombatantModel.combatant_id == combatant_id)
                 .with_for_update())
        result = await self.session.execute(query)
        combatant = result.scalar_one_or_none()
        if combatant is None:
            raise UpdateCombFailedError

        update_data = new_schema.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(combatant, field, value)

        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateCombFailedError
        return

    async def delete_combatant(self, combatant_id: UUID):
        query = (select(CombatantModel)
                 .where(CombatantModel.combatant_id == combatant_id)
                 .with_for_update())
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
