from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.character.enums import CharacterClass, Race
from src.models_core import Base, CreatureMixin, TimestampMixin


class CharacterModel(CreatureMixin, TimestampMixin, Base):
    __tablename__ = "characters"

    character_class: Mapped[CharacterClass] = mapped_column(Enum(CharacterClass, native_enum=False))
    race: Mapped[Race] = mapped_column(Enum(Race, native_enum=False))

    abilities: Mapped[list["AbilityModel"]] = relationship(
        "AbilityModel",
        back_populates="character",
        cascade="all, delete-orphan",
    )
