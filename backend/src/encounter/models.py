from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Enum, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.encounter.enums import CombatantStatus
from src.models_core import Base


class EncounterModel(Base):
    __tablename__ = 'encounters'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()
    round: Mapped[int] = mapped_column(default=0)
    current_turn: Mapped[int] = mapped_column(default=0)


class CombatantModel(Base):
    __tablename__ = "combatants"

    __table_args__ = (
        CheckConstraint(
            """
            (monster_id IS NOT NULL AND character_id IS NULL)
            OR
            (monster_id IS NULL AND character_id IS NOT NULL)
            """,
            name="ck_combatant_exactly_one_owner",
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    encounter_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="encounters.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    monster_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="monsters.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        nullable=True,
    )
    character_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="characters.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        nullable=True,
    )
    nickname: Mapped[str]
    current_hp: Mapped[int] = mapped_column(default=0)
    current_initiative: Mapped[int] = mapped_column(default=0)
    status: Mapped[CombatantStatus] = mapped_column(Enum(CombatantStatus, native_enum=False))
