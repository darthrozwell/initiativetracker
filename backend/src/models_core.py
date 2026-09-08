from datetime import datetime
from sqlalchemy import DateTime, Enum, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

from src.enums_core import CreatureAlignment, CreatureSource, DamageType, ConditionType, Skills


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class CreatureMixin:
    armor_class: Mapped[int] = mapped_column()  # 13 18 16
    initiative: Mapped[int] = mapped_column(default=0)  # only if it has proficiency 1, 2, 3...
    hit_points: Mapped[int] = mapped_column()  # average hit points 10, 66, 123...
    hit_points_formula: Mapped[str] = mapped_column() # "{X}d{Y} + {Z}"
    speed: Mapped[dict[str, int]] = mapped_column(JSONB, default=dict)  # "walk" : 30, "fly": 120,

    resistances: Mapped[list[DamageType]] = mapped_column(
        ARRAY(Enum(DamageType, native_enum=False)),
        default=list
    ) # ["cold"], ["psychic"], ["bludgeoning", "piercing"]
    immunities: Mapped[list[DamageType]] = mapped_column(
        ARRAY(Enum(DamageType, native_enum=False)),
        default=list
    ) # ["poison"], ["fire", "poison"], ["cold", "lightning"]
    vulnerabilities: Mapped[list[DamageType]] = mapped_column(
        ARRAY(Enum(DamageType, native_enum=False)),
        default=list
    ) # ["fire"], ["thunder"]
    condition_immunities: Mapped[list[ConditionType]] = mapped_column(
        ARRAY(Enum(ConditionType, native_enum=False)),
        default=list
    )  # ["poisoned"], ["frightened", "grappled", "paralyzed", "restrained"]

    strength: Mapped[int] = mapped_column()
    dexterity: Mapped[int] = mapped_column()
    constitution: Mapped[int] = mapped_column()
    intelligence: Mapped[int] = mapped_column()
    wisdom: Mapped[int] = mapped_column()
    charisma: Mapped[int] = mapped_column()
    saves: Mapped[dict[str, str]] = mapped_column(JSONB, default=dict) # {"str": "+6", "dex": "+5"}, {"dex": "+8", "wis": "+10}, {}

    name: Mapped[str] = mapped_column()
    alignment: Mapped[CreatureAlignment] = mapped_column(
        Enum(CreatureAlignment, native_enum=False)
    )
    source: Mapped[CreatureSource] = mapped_column(Enum(CreatureSource, native_enum=False))

    skills: Mapped[dict[Skills, str]] = mapped_column(JSONB, default=dict)  # {"perception": "+5", "stealth": "+7"}, {"arcana": "+7", "insight": "+6", "perception": "+6"}
    senses: Mapped[list[str]] = mapped_column(default=list)  # ["Darkvision 60 ft."], ["Darkvision 120 ft."], ["Truesight 120 ft."]
    languages: Mapped[list[str]] = mapped_column(default=list)  # ["Common"], ["Undercommon"], ["Infernal; telepathy 120 ft."], ["Deep Speech", "Undercommon; telepathy 120 ft."]
