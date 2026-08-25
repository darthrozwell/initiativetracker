from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models_core import Base, CreatureMixin, TimestampMixin
from src.monster.enums import MonsterType, MonsterSize, MonsterSource

class MonsterModel(CreatureMixin, TimestampMixin, Base):
    __tablename__ = "monsters"

    monster_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    source: Mapped[MonsterSource] = mapped_column(Enum(MonsterSource))
    size: Mapped[MonsterSize] = mapped_column(Enum(MonsterSize))
    creature_type: Mapped[MonsterType] = mapped_column(Enum(MonsterType))

    hit_points_formula: Mapped[str] = mapped_column()
    challenge_rating: Mapped[str] = mapped_column()
    experience: Mapped[int] = mapped_column()
    equipment: Mapped[str] = mapped_column()
    treasure: Mapped[str] = mapped_column()
    habitat: Mapped[str] = mapped_column()

    actions: Mapped[list["ActionModel"]] = relationship(
        "ActionModel",
        back_populates="monster",
        cascade="all, delete-orphan",
    )
