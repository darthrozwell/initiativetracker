from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.action.schemas import Damage
from src.action.enums import ActionType
from src.models_core import Base, TimestampMixin


class ActionModel(Base, TimestampMixin):
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

    action_id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    monster_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="monsters.monster_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable = True
    )
    character_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            column="characters.character_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True
    )
    type: Mapped[ActionType] = mapped_column()
    name: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
    range: Mapped[str] = mapped_column()
    reach: Mapped[str] = mapped_column()
    hit_bonus: Mapped[int] = mapped_column()
    damage: Mapped[list[Damage]] = mapped_column(
        JSONB,
        default=list,
    )

    monster: Mapped["MonsterModel"] = relationship(
        "MonsterModel",
        back_populates="actions",
    )

    character: Mapped["CharacterModel"] = relationship(
        "CharacterModel",
        back_populates="actions",
    )
