from enum import StrEnum


class CreatureAlignment(StrEnum):
    CHAOTIC_EVIL = "CE"
    CHAOTIC_NEUTRAL = "CN"
    CHAOTIC_GOOD = "CG"
    NEUTRAL_EVIL = "NE"
    NEUTRAL = "N"
    NEUTRAL_GOOD = "NG"
    LAWFUL_EVIL = "LE"
    LAWFUL_NEUTRAL = "LN"
    LAWFUL_GOOD = "LG"


class CreatureSize(StrEnum):
    TINY = "tiny"
    SMALL = "small"
    AVG = "average"
    BIG = "big"
    HUGE = "huge"
    GIANT = "giant"


class CreatureSource(StrEnum):
    CUSTOM = "custom"
    DMG = "Dungeon Master Guide 2024"
    ADV_IN_FAERUN = "Forgotten Realms: Adventures in Faerun"
    BOOK_OF_HUNGERS = "Astarion's Book of Hungers"
    LORWYN = "Lorwyn: First Light"
    MM = "Monster Manual 2024"
    NETHERIL = "Netheril's Fall"
    PHB = "Player's Handbook 2024"
    RAVENLOFT = "Ravenloft: The Horrors Within"


class DamageType(StrEnum):
    BLUDGEONING = "bludgeoning"
    PIERCING = "piercing"
    SLASHING = "slashing"
    ACID = "acid"
    COLD = "cold"
    FIRE = "fire"
    FORCE = "force"
    LIGHTNING = "lightning"
    NECROTIC = "necrotic"
    POISON = "poison"
    PSYCHIC = "psychic"
    RADIANT = "radiant"
    THUNDER = "thunder"


class ConditionType(StrEnum):
    UNCONSCIOUS = "unconscious"
    FRIGHTENED = "frightened"
    EXHAUSTION = "exhaustion"
    INVISIBLE = "invisible"
    INCAPACITATED = "incapacitated"
    DEAFENED = "deafened"
    PETRIFIED = "petrified"
    PRONE = "prone"
    RESTRAINED = "restrained"
    BLINDED = "blinded"
    POISONED = "poisoned"
    CHARMED = "charmed"
    STUNNED = "stunned"
    PARALYZED = "paralyzed"
    GRAPPLED = "grappled"


class Skills(StrEnum):
    ACROBATICS = "acrobatics"
    ANIMAL_HANDLING = "animal_handling"
    ARCANA = "arcana"
    ATHLETICS = "athletics"
    DECEPTION = "deception"
    HISTORY = "history"
    INSIGHT = "insight"
    INTIMIDATION = "intimidation"
    INVESTIGATION = "investigation"
    MEDICINE = "medicine"
    NATURE = "nature"
    PERCEPTION = "perception"
    PERFORMANCE = "performance"
    PERSUASION = "persuasion"
    RELIGION = "religion"
    SLEIGHT_OF_HAND = "sleight_of_hand"
    STEALTH = "stealth"
    SURVIVAL = "survival"
