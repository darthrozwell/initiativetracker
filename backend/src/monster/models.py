from sqlalchemy import Enum, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models_core import Base, CreatureMixin, TimestampMixin
from src.monster.enums import MonsterType


class MonsterModel(CreatureMixin, TimestampMixin, Base):
    __tablename__ = "monsters"

    type: Mapped[MonsterType] = mapped_column(Enum(MonsterType, native_enum=False))
    challenge_rating: Mapped[str] = mapped_column()
    equipment: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    treasure: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    environment: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)

    abilities: Mapped[list["AbilityModel"]] = relationship(
        "AbilityModel",
        back_populates="monster",
        cascade="all, delete-orphan",
    )
