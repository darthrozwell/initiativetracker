from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from models_core import Base


class MonsterModel(Base):
    __tablename__ = "monsters"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    source: Mapped[str] = mapped_column(nullable=True)
    size: Mapped[str] = mapped_column(nullable=True)
    creature_type: Mapped[str] = mapped_column(nullable=True)
    alignment: Mapped[str] = mapped_column(nullable=True)
    info: Mapped[dict] = mapped_column(JSON, nullable=True)
    abilities: Mapped[list] = mapped_column(JSON, nullable=True)
    stats: Mapped[dict] = mapped_column(JSON, nullable=True)

    armor_class: Mapped[str] = mapped_column(nullable=True)  # "Класс Защиты": "16",
    initiative: Mapped[str] = mapped_column(nullable=True)  # "Инициатива": "+3 (13)",
    hp: Mapped[str] = mapped_column(nullable=True)  # "Хиты": "66 (12к8 + 12)",
    movement: Mapped[str] = mapped_column(nullable=True)  # "Скорость": "20 футов, Полёта 50 футов",
    skills: Mapped[str] = mapped_column(nullable=True)  # "Навыки": "Восприятие +7, Природа +5, Тайная магия +3",
    resistances: Mapped[str] = mapped_column(nullable=True)  # Сопротивление урону
    immunities: Mapped[str] = mapped_column(nullable=True)  # Иммунитеты
    senses: Mapped[str] = mapped_column(nullable=True)  # "Чувства": "пассивное Восприятие 17",
    languages: Mapped[str] = mapped_column(nullable=True)  # "Языки": "Первичный (Ауран), Язык Ааракокра",
    areal: Mapped[str] = mapped_column(nullable=True)  # "Среда обитания": "Горы, Стихийный план Воздуха",
    gear: Mapped[str] = mapped_column(nullable=True)  # Снаряжение
    loot: Mapped[str] = mapped_column(nullable=True)  # "Сокровища": "Личные , Инструментальные",
    danger: Mapped[str] = mapped_column(nullable=True)  # "Опасность": "4 (1 100 опыта; БВ +2)"

    strength: Mapped[int] = mapped_column(nullable=True)
    dexterity: Mapped[int] = mapped_column(nullable=True)
    constitution: Mapped[int] = mapped_column(nullable=True)
    intelligence: Mapped[int] = mapped_column(nullable=True)
    wisdom: Mapped[int] = mapped_column(nullable=True)
    charisma: Mapped[int] = mapped_column(nullable=True)
    strength_save: Mapped[str] = mapped_column(nullable=True)
    dexterity_save: Mapped[str] = mapped_column(nullable=True)
    constitution_save: Mapped[str] = mapped_column(nullable=True)
    intelligence_save: Mapped[str] = mapped_column(nullable=True)
    wisdom_save: Mapped[str] = mapped_column(nullable=True)
    charisma_save: Mapped[str] = mapped_column(nullable=True)
