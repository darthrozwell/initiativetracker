from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.character.enums import CharacterClass, Race
from src.models_core import Base, CreatureMixin, TimestampMixin


class CharacterModel(CreatureMixin, TimestampMixin, Base):
    __tablename__ = "characters"

    character_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    character_class: Mapped[CharacterClass] = mapped_column(Enum(CharacterClass))
    race: Mapped[Race] = mapped_column(Enum(Race))

    actions: Mapped[list["ActionModel"]] = relationship(
        "ActionModel",
        back_populates="character",
        cascade="all, delete-orphan",
    )
