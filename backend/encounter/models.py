from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from models_core import Base


class EncounterModel(Base):
    __tablename__ = 'encounter'

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    round: Mapped[int] = mapped_column(default=0)
    current_turn: Mapped[int] = mapped_column(default=0)
    combatants: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    history: Mapped[list[dict]] = mapped_column(JSON, nullable=True)
    settings: Mapped[dict] = mapped_column(JSON, nullable=True)
