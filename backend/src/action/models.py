from uuid import UUID, uuid4
from sqlalchemy import CheckConstraint, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums_core import ConditionType
from src.action.enums import AbilityType, AbilityDistance, HitMethod, SaveEffect
from src.action.schemas import Damage
from src.models_core import Base


class AbilityModel(Base):
    __tablename__ = 'actions'

    __table_args__ = (
        CheckConstraint(
            """
            (monster_id IS NOT NULL AND character_id IS NULL)
            OR
            (monster_id IS NULL AND character_id IS NOT NULL)
            """,
            name="ck_action_exactly_one_owner",
        ),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    monster_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="monsters.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable = True
    )
    character_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="characters.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )


    type: Mapped[AbilityType] = mapped_column(
        Enum(AbilityType, native_enum=False),
    )
    name: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
    distance: Mapped[dict[AbilityDistance, int]] = mapped_column(JSONB, default=dict) # {range: 50 }, {emanation: 20}, numbers in foots
    hit_method: Mapped[HitMethod] = mapped_column(Enum(HitMethod, native_enum=False))
    hit_bonus: Mapped[int | None] = mapped_column(nullable=True)
    dc: Mapped[int | None] = mapped_column(nullable=True)
    on_successful_save: Mapped[list[SaveEffect] | None] = mapped_column(ARRAY(Enum(SaveEffect, native_enum=False)), nullable=True)
    damage: Mapped[list[Damage] | None] = mapped_column(JSONB, nullable=True)
    condition: Mapped[list[ConditionType] | None] = mapped_column(ARRAY(Enum(ConditionType, native_enum=False)), nullable=True)


    monster: Mapped["MonsterModel"] = relationship(
        "MonsterModel",
        back_populates="abilities",
    )

    character: Mapped["CharacterModel"] = relationship(
        "CharacterModel",
        back_populates="abilities",
    )
