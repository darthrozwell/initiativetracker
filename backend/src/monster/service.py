from uuid import UUID

from asyncpg import PostgresError
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.damage.models import DamageResistanceModel, DamageVulnerabilityModel, ImmunityModel
from src.action.models import ActionModel
from src.monster.exceptions import AddFailedError, AddAttackFailedError, UpdateFailedError, UpdateAttackFailedError, \
    DeleteFailedError, DeleteNotFoundError
from src.monster.models import MonsterModel
from src.monster.schemas import MonsterInSchema, MonsterUpdateSchema


class MonsterService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_by_name(self, name: str) -> MonsterModel | None:
        query = (select(MonsterModel)
                 .where(MonsterModel.name == name)
                 .options(selectinload(MonsterModel.actions),
                 selectinload(MonsterModel.damage_immunity),
                 selectinload(MonsterModel.damage_vulnerability),
                 selectinload(MonsterModel.damage_resistance)))
        result = await self.session.execute(query)
        return result.scalars().first()


    async def get_all(self):
        query = (select(MonsterModel)
                 .options(selectinload(MonsterModel.actions),
                 selectinload(MonsterModel.damage_immunity),
                 selectinload(MonsterModel.damage_vulnerability),
                 selectinload(MonsterModel.damage_resistance))
                 .order_by(MonsterModel.name))
        result = await self.session.execute(query)
        return result.scalars().all()


    async def create(self, monster_schema: MonsterInSchema):
        new_monster = MonsterModel(**monster_schema.model_dump(exclude={"actions", "protections"}))
        for action in monster_schema.actions:
            new_action = ActionModel(**action.model_dump())
            new_monster.actions.append(new_action)
        new_monster.damage_resistance = [DamageResistanceModel(resistance=resistance) for resistance in monster_schema.protections.damage_resistance]
        new_monster.damage_vulnerability = [DamageVulnerabilityModel(vulnerability=vulnerability) for vulnerability in monster_schema.protections.damage_vulnerability]
        new_monster.damage_immunity = [ImmunityModel(immunity=immunity) for immunity in monster_schema.protections.damage_immunity]
        self.session.add(new_monster)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise AddFailedError

        await self.session.refresh(new_monster, [
            "damage_resistance",
            "damage_vulnerability",
            "damage_immunity",
            "actions",
        ])
        return new_monster


    async def update(self, monster_id: UUID, monster_schema: MonsterUpdateSchema):
        query = (select(MonsterModel)
                 .where(MonsterModel.monster_id == monster_id)
                 .options(selectinload(MonsterModel.actions),
                          selectinload(MonsterModel.damage_immunity),
                          selectinload(MonsterModel.damage_resistance),
                          selectinload(MonsterModel.damage_vulnerability))
                 .with_for_update())
        result = await self.session.execute(query)
        monster = result.scalar_one_or_none()
        if monster is None:
            raise UpdateFailedError

        update_data = monster_schema.model_dump(exclude_unset=True, exclude={"actions", "protections"})
        for field, value in update_data.items():
            setattr(monster, field, value)

        if monster_schema.protections is not None:
            monster.damage_resistance = [
                DamageResistanceModel(resistance=x)
                for x in monster_schema.protections.damage_resistance
            ]
            monster.damage_vulnerability = [
                DamageVulnerabilityModel(vulnerability=x)
                for x in monster_schema.protections.damage_vulnerability
            ]
            monster.damage_immunity = [
                ImmunityModel(immunity=x)
                for x in monster_schema.protections.damage_immunity
            ]

        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise UpdateFailedError

        return


    async def delete(self, monster_id: UUID):
        query = (select(MonsterModel).
                 where(MonsterModel.monster_id == monster_id).
                 with_for_update())
        result = await self.session.execute(query)
        monster = result.scalar_one_or_none()
        if monster is None:
            raise DeleteNotFoundError
        try:
            await self.session.delete(monster)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise DeleteFailedError
