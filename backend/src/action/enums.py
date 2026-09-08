from enum import StrEnum


class AbilityType(StrEnum):
    ACTION = "action"
    BONUS_ACTION = "bonus_action"
    REACTION = "reaction"
    SPELLCASTING = "spellcasting"
    LEGENDARY_ACTION = "legendary_action"
    TRAIT = "trait"


class AbilityDistance(StrEnum):
    REACH = "reach"
    RANGE = "range"
    EMANATION = "emanation"
    CONE = "cone"
    CUBE = "cube"
    LINE = "line"
    SPHERE = "sphere"
    CYLINDER = "cylinder"


class HitMethod(StrEnum):
    ROLL = "roll"
    SAVE = "save"
    ROLL_THEN_SAVE = "roll_then_save"
    AUTO = "auto"


class SaveEffect(StrEnum):
    HALF_DMG = "half_dmg"
    NO_DMG = "no_dmg"
    NO_CONDITION = "no_condition"
