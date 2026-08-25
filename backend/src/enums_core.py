from enum import StrEnum


class CreatureAlignment(StrEnum):
    CHAOTIC_EVIL = "Хаотичный Злой"
    CHAOTIC_NEUTRAL = "Хаотичный Нейтральный"
    CHAOTIC_GOOD = "Хаотичный Добрый"
    NEUTRAL_EVIL = "Нейтральный Злой"
    NEUTRAL = "Нейтральный"
    NEUTRAL_GOOD = "Нейтральный Добрый"
    LAWFUL_EVIL = "Принципиальный Злой"
    LAWFUL_NEUTRAL = "Принципиальный Нейтральный"
    LAWFUL_GOOD = "Принципиальный Добрый"


class DamageType(StrEnum):
    BLUDGEONING = "Дробящий"
    PIERCING = "Колющий"
    SLASHING = "Рубящий"
    ACID = "Кислота"
    COLD = "Холод"
    FIRE = "Огонь"
    FORCE = "Силовой"
    LIGHTNING = "Электричество"
    NECROTIC = "Некротический"
    POISON = "Яд"
    PSYCHIC = "Психический"
    RADIANT = "Излучение"
    THUNDER = "Звук"


class ConditionType(StrEnum):
    UNCONSCIOUS = "Бессознательный"
    FRIGHTENED = "Испуганный"
    EXHAUSTION = "Истощение"
    INVISIBLE = "Невидимый"
    INCAPACITATED = "Недееспособный"
    DEAFENED = "Оглохший"
    PETRIFIED = "Окаменевший"
    PRONE = "Опрокинутый"
    RESTRAINED = "Опутанный"
    BLINDED = "Ослеплённый"
    POISONED = "Отравленный"
    CHARMED = "Очарованный"
    STUNNED = "Ошеломлённый"
    PARALYZED = "Парализованный"
    GRAPPLED = "Схваченный"
