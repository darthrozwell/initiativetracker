from uuid import uuid4, UUID
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.action.models import AbilityModel
from src.character.exceptions import AddCharacterFailedError, UpdateCharacterFailedError, DeleteCharacterFailedError, \
    AddAttackFailedError, UpdateAttackFailedError, DeleteCharacterNotFoundError
from src.character.models import CharacterModel
from src.character.schemas import CharacterInSchema, CharacterUpdateSchema


class CharacterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_id(self, character_id: UUID) -> CharacterModel | None:
        query = (select(CharacterModel)
                 .where(CharacterModel.id == character_id)
                 .options(selectinload(CharacterModel.abilities)))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def get_all(self) -> list[CharacterModel]:
        query = (select(CharacterModel)
                 .options(selectinload(CharacterModel.abilities))
                 .order_by(CharacterModel.name))
        result = await self.session.execute(query)
        return list(result.scalars().all())


    async def create(self, character: CharacterInSchema) -> CharacterModel | None:
        new_character = CharacterModel(
            **character.model_dump(exclude={"abilities"}),
            abilities=[
                AbilityModel(**ability.model_dump())
                for ability in character.abilities
            ]
        )
        self.session.add(new_character)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddCharacterFailedError

        await self.session.refresh(new_character, [
            "abilities",
        ])
        return new_character


    async def update(self, character_id: UUID, data: CharacterUpdateSchema) -> CharacterModel | None:
        query = (select(CharacterModel)
                 .where(CharacterModel.id == character_id)
                 .options(selectinload(CharacterModel.abilities))
                 .with_for_update())
        result = await self.session.execute(query)
        character = result.scalar_one_or_none()
        if character is None:
            raise UpdateCharacterFailedError

        update_data = data.model_dump(exclude_unset=True, exclude={"abilities"})
        for field, value in update_data.items():
            setattr(character, field, value)

        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateCharacterFailedError

        await self.session.refresh(character, [
            "abilities",
        ])

        return character


    async def delete(self, character_id: UUID):
        query = (select(CharacterModel)
                 .where(CharacterModel.id == character_id)
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
