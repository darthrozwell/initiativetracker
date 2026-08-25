from uuid import UUID, uuid4

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.character.enums import CharacterClass, Race
from src.models_core import Base, CreatureMixin, TimestampMixin


class CharacterModel(CreatureMixin, TimestampMixin, Base):
    __tablename__ = "characters"

    character_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True)
    character_class: Mapped[CharacterClass] = mapped_column(Enum(CharacterClass))
    race: Mapped[Race] = mapped_column(Enum(Race))

    actions: Mapped[list["ActionModel"]] = relationship(
        "ActionModel",
        back_populates="character",
        cascade="all, delete-orphan",
    )
    damage_resistance: Mapped[list["DamageResistanceModel"]] = relationship(
        "DamageResistanceModel",
        back_populates="character",
        cascade="all, delete-orphan",
    )
    damage_immunity: Mapped[list["ImmunityModel"]] = relationship(
        "ImmunityModel",
        back_populates="character",
        cascade="all, delete-orphan",
    )
    damage_vulnerability: Mapped[list["DamageVulnerabilityModel"]] = relationship(
        "DamageVulnerabilityModel",
        back_populates="character",
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
