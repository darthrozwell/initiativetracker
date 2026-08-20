from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.character.enums import CharacterClass, Race
from src.models_core import Base


class CharacterModel(Base):
    __tablename__ = "characters"

    character_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    character_class: Mapped[CharacterClass] = mapped_column(Enum(CharacterClass))
    race: Mapped[Race] = mapped_column(Enum(Race))

    armor_class: Mapped[int] = mapped_column()  # "Класс Защиты": "16",
    initiative: Mapped[int] = mapped_column()  # "Инициатива": "+3 (13)",
    speed: Mapped[str] = mapped_column()  # "Скорость": "20 футов, Полёта 50 футов",
    hit_points_value: Mapped[int] = mapped_column()  # "Хиты": "66 (12к8 + 12)",
    damage_resistance: Mapped[str] = mapped_column()
    damage_immunity: Mapped[str] = mapped_column()
    damage_vulnerability: Mapped[str] = mapped_column()

    strength_value: Mapped[int] = mapped_column()
    strength_mod: Mapped[int] = mapped_column()
    strength_save: Mapped[int] = mapped_column()
    dexterity_value: Mapped[int] = mapped_column()
    dexterity_mod: Mapped[int] = mapped_column()
    dexterity_save: Mapped[int] = mapped_column()
    constitution_value: Mapped[int] = mapped_column()
    constitution_mod: Mapped[int] = mapped_column()
    constitution_save: Mapped[int] = mapped_column()
    intelligence_value: Mapped[int] = mapped_column()
    intelligence_mod: Mapped[int] = mapped_column()
    intelligence_save: Mapped[int] = mapped_column()
    wisdom_value: Mapped[int] = mapped_column()
    wisdom_mod: Mapped[int] = mapped_column()
    wisdom_save: Mapped[int] = mapped_column()
    charisma_value: Mapped[int] = mapped_column()
    charisma_mod: Mapped[int] = mapped_column()
    charisma_save: Mapped[int] = mapped_column()

    abilities: Mapped[list["CharacterAttackModel"]] = relationship(
        "CharacterAttackModel",
        back_populates="character_rel",
        lazy="selectin",
        cascade="all, delete-orphan",
    )


class CharacterAttackModel(Base):
    __tablename__ = "character_attacks"

    attack_id: Mapped[str] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(
        ForeignKey(
            column="characters.name",
            ondelete="CASCADE",
            onupdate="CASCADE",
        )
    )
    title: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
    attack_type: Mapped[str] = mapped_column()
    attack_range: Mapped[str] = mapped_column()
    hit_bonus: Mapped[int] = mapped_column()
    reach: Mapped[str] = mapped_column()
    damage: Mapped[str] = mapped_column()

    character_rel: Mapped["CharacterModel"] = relationship(
        "CharacterModel",
        back_populates="abilities",
    )
