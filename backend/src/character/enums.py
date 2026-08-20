from enum import StrEnum


class Race(StrEnum):
    AASIMAR = "AASIMAR"
    GNOME = "GNOME"
    GOLIATH = "GOLIATH"
    DWARF = "DWARF"
    DRAGONBORN = "DRAGONBORN"
    ORC = "ORC"
    HALFLING = "HALFLING"
    TIEFLING = "TIEFLING"
    HUMAN = "HUMAN"
    ELF = "ELF"


class CharacterClass(StrEnum):
    ARTIFICER = "ARTIFICER"
    BARD = "BARD"
    BARBARIAN = "BARBARIAN"
    FIGHTER = "FIGHTER"
    WIZARD = "WIZARD"
    DRUID = "DRUID"
    CLERIC = "CLERIC"
    WARLOCK = "WARLOCK"
    MONK = "MONK"
    PALADIN = "PALADIN"
    ROGUE = "ROGUE"
    RANGER = "RANGER"
    SORCERER = "SORCERER"
