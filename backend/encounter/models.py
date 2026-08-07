from operator import gt

from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models_core import Base
from monster.models import MonsterModel


class EncounterModel(Base):
    __tablename__ = 'encounter'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    round: Mapped[int] = mapped_column(default=1)
    current_turn: Mapped[int] = mapped_column(default=0)
    combatants: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    history: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    settings: Mapped[dict] = mapped_column(JSON, nullable=True)


class CombatantModel(Base):
    __tablename__ = "combatants"

    id: Mapped[str] = mapped_column(primary_key=True)
    encounter_id: Mapped[str] = mapped_column(
        ForeignKey(
            column="encounter.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    monster_id: Mapped[str] = mapped_column(
        ForeignKey(
            column="monsters.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )

    nickname: Mapped[str] = mapped_column()
    current_hp: Mapped[int] = mapped_column(default=0)
    status: Mapped[str]
