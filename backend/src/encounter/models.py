from sqlalchemy import JSON, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.encounter.enums import CombatantStatus
from src.models_core import Base


class EncounterModel(Base):
    __tablename__ = 'encounter'

    encounter_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    round: Mapped[int] = mapped_column(default=1)
    current_turn: Mapped[int] = mapped_column(default=0)


class CombatantModel(Base):
    __tablename__ = "combatants"

    combatant_id: Mapped[str] = mapped_column(primary_key=True)
    encounter_id: Mapped[str] = mapped_column(
        ForeignKey(
            column="encounter.encounter_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    monster_id: Mapped[str] = mapped_column(
        ForeignKey(
            column="monsters.monster_id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )
    nickname: Mapped[str]
    current_hp: Mapped[int] = mapped_column(default=0)
    status: Mapped[CombatantStatus] = mapped_column(Enum(CombatantStatus))
