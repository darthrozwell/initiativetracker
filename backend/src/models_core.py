from datetime import datetime
from sqlalchemy import DateTime, func, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.enums_core import CreatureAlignment


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class CreatureMixin:
    alignment: Mapped[CreatureAlignment] = mapped_column(Enum(CreatureAlignment))

    armor_class: Mapped[int] = mapped_column()  # "Класс Защиты": "16",
    initiative: Mapped[int] = mapped_column()  # "Инициатива": "+3 (13)",
    hit_points_value: Mapped[int] = mapped_column()  # "Хиты": "66 (12к8 + 12)",
    speed: Mapped[str] = mapped_column()  # "Скорость": "20 футов, Полёта 50 футов",
    skills: Mapped[str] = mapped_column()  # "Навыки": "Восприятие +7, Природа +5, Тайная магия +3",
    senses: Mapped[str] = mapped_column()  # "Чувства": "пассивное Восприятие 17",
    languages: Mapped[str] = mapped_column()  # "Языки": "Первичный (Ауран), Язык Ааракокра",
    proficiency_bonus: Mapped[int] = mapped_column()

    strength_value: Mapped[int] = mapped_column()
    is_strength_save: Mapped[bool] = mapped_column()
    dexterity_value: Mapped[int] = mapped_column()
    is_dexterity_save: Mapped[bool] = mapped_column()
    constitution_value: Mapped[int] = mapped_column()
    is_constitution_save: Mapped[bool] = mapped_column()
    intelligence_value: Mapped[int] = mapped_column()
    is_intelligence_save: Mapped[bool] = mapped_column()
    wisdom_value: Mapped[int] = mapped_column()
    is_wisdom_save: Mapped[bool] = mapped_column()
    charisma_value: Mapped[int] = mapped_column()
    is_charisma_save: Mapped[bool] = mapped_column()
