from uuid import uuid4, UUID

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.damage.models import DamageResistanceModel, DamageVulnerabilityModel, ImmunityModel
from src.action.models import ActionModel
from src.character.exceptions import AddCharacterFailedError, UpdateCharacterFailedError, DeleteCharacterFailedError, \
    AddAttackFailedError, UpdateAttackFailedError, DeleteCharacterNotFoundError
from src.character.models import CharacterModel
from src.character.schemas import CharacterInSchema, CharacterUpdateSchema


class CharacterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_id(self, character_id: UUID) -> CharacterModel | None:
        query = (select(CharacterModel)
                 .where(CharacterModel.character_id == character_id)
                 .options(selectinload(CharacterModel.actions),
                          selectinload(CharacterModel.damage_immunity),
                          selectinload(CharacterModel.damage_resistance),
                          selectinload(CharacterModel.damage_vulnerability)))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def get_all(self):
        query = (select(CharacterModel)
                 .options(selectinload(CharacterModel.actions),
                          selectinload(CharacterModel.damage_immunity),
                          selectinload(CharacterModel.damage_resistance),
                          selectinload(CharacterModel.damage_vulnerability))
                 .order_by(CharacterModel.name))
        result = await self.session.execute(query)
        return result.scalars().all()


    async def create(self, character: CharacterInSchema):
        new_character = CharacterModel(**character.model_dump(exclude={"actions", "protections"}))
        for action in character.actions:
            new_action = ActionModel(**action.model_dump())
            new_character.actions.append(new_action)
        new_character.damage_resistance = [DamageResistanceModel(resistance=resistance) for resistance in character.protections.damage_resistance]
        new_character.damage_vulnerability = [DamageVulnerabilityModel(vulnerability=vulnerability) for vulnerability in character.protections.damage_vulnerability]
        new_character.damage_immunity = [ImmunityModel(immunity=immunity) for immunity in character.protections.damage_immunity]
        self.session.add(new_character)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddCharacterFailedError

        await self.session.refresh(new_character, [
            "damage_resistance",
            "damage_vulnerability",
            "damage_immunity",
            "actions",
        ])
        return new_character


    async def update(self, character_id: UUID, data: CharacterUpdateSchema):
        query = (select(CharacterModel)
                 .where(CharacterModel.character_id == character_id)
                 .options(selectinload(CharacterModel.actions),
                          selectinload(CharacterModel.damage_immunity),
                          selectinload(CharacterModel.damage_resistance),
                          selectinload(CharacterModel.damage_vulnerability))
                 .with_for_update())
        result = await self.session.execute(query)
        character = result.scalar_one_or_none()
        if character is None:
            raise UpdateCharacterFailedError

        update_data = data.model_dump(exclude_unset=True, exclude={"actions", "protections"})
        for field, value in update_data.items():
            setattr(character, field, value)

        if data.protections is not None:
            character.damage_resistance = [
                DamageResistanceModel(resistance=x)
                for x in data.protections.damage_resistance
            ]
            character.damage_vulnerability = [
                DamageVulnerabilityModel(vulnerability=x)
                for x in data.protections.damage_vulnerability
            ]
            character.damage_immunity = [
                ImmunityModel(immunity=x)
                for x in data.protections.damage_immunity
            ]

        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateCharacterFailedError

        return


    async def delete(self, character_id: UUID):
        query = (select(CharacterModel)
                 .where(CharacterModel.character_id == character_id)
                 .with_for_update())
        result = await self.session.execute(query)
        character = result.scalar_one_or_none()
        if character is None:
            raise DeleteCharacterNotFoundError
        try:
            await self.session.delete(character)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise DeleteCharacterFailedError
        return
