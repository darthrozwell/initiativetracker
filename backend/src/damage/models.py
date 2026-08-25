from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, ForeignKey, Enum, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models_core import Base, TimestampMixin
from src.enums_core import DamageType, ConditionType


class DamageResistanceModel(Base, TimestampMixin):
    __tablename__ = 'damage_resistances'

    __table_args__ = (
        CheckConstraint(
            """
            (monster_id IS NOT NULL AND character_id IS NULL)
            OR
            (monster_id IS NULL AND character_id IS NOT NULL)
            """,
            name="ck_resistance_exactly_one_owner",
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    monster_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="monsters.monster_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )
    character_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="characters.character_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )

    resistance: Mapped[DamageType] = mapped_column(Enum(DamageType))

    monster: Mapped["MonsterModel"] = relationship(
        "MonsterModel",
        back_populates="damage_resistance",
    )

    character: Mapped["CharacterModel"] = relationship(
        "CharacterModel",
        back_populates="damage_resistance",
    )

class DamageVulnerabilityModel(Base, TimestampMixin):
    __tablename__ = 'damage_vulnerabilities'

    __table_args__ = (
        CheckConstraint(
            """
            (monster_id IS NOT NULL AND character_id IS NULL)
            OR
            (monster_id IS NULL AND character_id IS NOT NULL)
            """,
            name="ck_vulnerability_exactly_one_owner",
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    monster_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="monsters.monster_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )
    character_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="characters.character_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )

    vulnerability: Mapped[DamageType] = mapped_column(Enum(DamageType))

    monster: Mapped["MonsterModel"] = relationship(
        "MonsterModel",
        back_populates="damage_vulnerability",
    )

    character: Mapped["CharacterModel"] = relationship(
        "CharacterModel",
        back_populates="damage_vulnerability",
    )


class ImmunityModel(Base, TimestampMixin):
    __tablename__ = 'immunities'

    __table_args__ = (
        CheckConstraint(
            """
            (monster_id IS NOT NULL AND character_id IS NULL)
            OR
            (monster_id IS NULL AND character_id IS NOT NULL)
            """,
            name="ck_immunity_exactly_one_owner",
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    monster_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="monsters.monster_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )
    character_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="characters.character_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )

    immunity: Mapped[DamageType | ConditionType] = mapped_column(String)

    monster: Mapped["MonsterModel"] = relationship(
        "MonsterModel",
        back_populates="damage_immunity",
    )

    character: Mapped["CharacterModel"] = relationship(
        "CharacterModel",
        back_populates="damage_immunity",
    )
