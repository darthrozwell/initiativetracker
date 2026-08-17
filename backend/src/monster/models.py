from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models_core import Base
from src.monster.enums import MonsterType, MonsterAlignment, MonsterSize, MonsterSource

class MonsterModel(Base):
    __tablename__ = "monsters"

    monster_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    source: Mapped[MonsterSource] = mapped_column(Enum(MonsterSource))
    size: Mapped[MonsterSize] = mapped_column(Enum(MonsterSize))
    creature_type: Mapped[MonsterType] = mapped_column(Enum(MonsterType))
    alignment: Mapped[MonsterAlignment] = mapped_column(Enum(MonsterAlignment))

    armor_class: Mapped[int] = mapped_column()  # "Класс Защиты": "16",
    initiative: Mapped[int] = mapped_column()  # "Инициатива": "+3 (13)",
    hit_points_value: Mapped[int] = mapped_column()  # "Хиты": "66 (12к8 + 12)",
    hit_points_formula: Mapped[str] = mapped_column()
    speed: Mapped[str] = mapped_column()  # "Скорость": "20 футов, Полёта 50 футов",
    skills: Mapped[str] = mapped_column()  # "Навыки": "Восприятие +7, Природа +5, Тайная магия +3",
    damage_resistance: Mapped[str] = mapped_column()
    damage_immunity: Mapped[str] = mapped_column()
    damage_vulnerability: Mapped[str] = mapped_column()
    senses: Mapped[str] = mapped_column()  # "Чувства": "пассивное Восприятие 17",
    languages: Mapped[str] = mapped_column()  # "Языки": "Первичный (Ауран), Язык Ааракокра",
    challenge_rating: Mapped[str] = mapped_column()
    experience: Mapped[int] = mapped_column()
    proficiency_bonus: Mapped[int] = mapped_column()
    equipment: Mapped[str] = mapped_column()
    treasure: Mapped[str] = mapped_column()
    habitat: Mapped[str] = mapped_column()

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

    abilities: Mapped[list["MonsterAttackModel"]] = relationship(
        "MonsterAttackModel",
        back_populates="monster",
        lazy="selectin",
        cascade="all, delete-orphan",
    )



class MonsterAttackModel(Base):
    __tablename__ = "monster_attacks"

    attack_id: Mapped[str] = mapped_column(primary_key=True)
    monster_name: Mapped[str] = mapped_column(
        ForeignKey(
            column="monsters.name",
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

    monster: Mapped["MonsterModel"] = relationship(
        "MonsterModel",
        back_populates="abilities",
    )
