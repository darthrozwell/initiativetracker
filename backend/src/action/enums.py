from enum import StrEnum


class ActionType(StrEnum):
    ACTION = "Действия"
    BONUS_ACTION = "Бонусные действия"
    REACTION = "Реакции"
    LEGENDARY_ACTION = "Легендарные действия"
    FEATURE = "Особенности"


class DamageType(StrEnum):
    BLUDGEONING = "Дробящий урон"
    PIERCING = "Колющий урон"
    SLASHING = "Рубящий урон"
    ACID = "урон Кислотой"
    COLD = "урон Холодом"
    FIRE = "урон Огнём"
    FORCE = "Силовой урон"
    LIGHTNING = "урон Электричеством"
    NECROTIC = "Некротический урон"
    POISON = "урон Ядом"
    PSYCHIC = "Психический урон"
    RADIANT = "урон Излучением"
    THUNDER = "урон Звуком"
