from uuid import uuid4

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.character.exceptions import AddCharacterFailedError, UpdateCharacterFailedError, DeleteCharacterFailedError, \
    AddAttackFailedError, UpdateAttackFailedError, DeleteCharacterNotFoundError
from src.character.models import CharacterModel, CharacterAttackModel
from src.character.schemas import CharacterInSchema, CharacterUpdateSchema


class CharacterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_id(self, character_id: str) -> CharacterModel | None:
        query = select(CharacterModel).where(CharacterModel.character_id == character_id).options(selectinload(CharacterModel.abilities))
        result = await self.session.execute(query)
        return result.scalar_one_or_none()


    async def get_all(self):
        query = select(CharacterModel).options(selectinload(CharacterModel.abilities)).order_by(CharacterModel.name)
        result = await self.session.execute(query)
        return result.scalars().all()


    async def create(self, character: CharacterInSchema):
        new_character = CharacterModel(**character.model_dump(exclude={"abilities"}))
        new_character.character_id = str(uuid4())
        self.session.add(new_character)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddCharacterFailedError

        if character.abilities is not None:
            for data_abilities in character.abilities:
                new_ability = CharacterAttackModel(**data_abilities.model_dump())
                new_ability.attack_id = str(uuid4())
                new_ability.character_name = new_character.name
                self.session.add(new_ability)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddAttackFailedError

        result = await self.session.execute(
            select(CharacterModel)
            .options(selectinload(CharacterModel.abilities))
            .where(CharacterModel.character_id == new_character.character_id)
        )
        new_character = result.scalar_one()
        return new_character


    async def update(self, character_id:str, data: CharacterUpdateSchema):
        query = update(CharacterModel).where(CharacterModel.character_id == character_id).values(**data.model_dump(exclude_unset=True, exclude={"abilities"}))
        result = await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateCharacterFailedError

        if data.abilities is not None:
            for data_abilities in data.abilities:
                query = update(CharacterAttackModel).where(CharacterAttackModel.character_name == data.name).values(**data_abilities.model_dump())
                result = await self.session.execute(query)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateAttackFailedError

        return


    async def delete(self, character_id:str):
        query = select(CharacterModel).where(CharacterModel.character_id == character_id).with_for_update()
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
