from uuid import uuid4, UUID

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models_core import Base, CreatureMixin, TimestampMixin
from src.damage.models import DamageResistanceModel, DamageVulnerabilityModel, ImmunityModel
from src.monster.enums import MonsterType, MonsterSize, MonsterSource

class MonsterModel(CreatureMixin, TimestampMixin, Base):
    __tablename__ = "monsters"

    monster_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
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
    damage_resistance: Mapped[list["DamageResistanceModel"]] = relationship(
        "DamageResistanceModel",
        back_populates="monster",
        cascade="all, delete-orphan",
    )
    damage_immunity: Mapped[list["ImmunityModel"]] = relationship(
        "ImmunityModel",
        back_populates="monster",
        cascade="all, delete-orphan",
    )
    damage_vulnerability: Mapped[list[DamageVulnerabilityModel]] = relationship(
        "DamageVulnerabilityModel",
        back_populates="monster",
        cascade="all, delete-orphan",
    )

    @property
    def protections(self):
        return {
            "damage_resistance": [
                x.resistance for x in self.damage_resistance
            ],
            "damage_vulnerability": [
                x.vulnerability for x in self.damage_vulnerability
            ],
            "damage_immunity": [
                x.immunity for x in self.damage_immunity
            ],
        }
