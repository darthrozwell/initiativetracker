from enum import StrEnum


class Race(StrEnum):
    AASIMAR = "Aasimar"
    GNOME = "Gnome"
    GOLIATH = "Goliath"
    DWARF = "Dwarf"
    DRAGONBORN = "Dragonborn"
    ORC = "Orc"
    HALFLING = "Halfling"
    TIEFLING = "Tiefling"
    HUMAN = "Human"
    ELF = "Elf"


class CharacterClass(StrEnum):
    ARTIFICER = "Artificer"
    BARD = "Bard"
    BARBARIAN = "Barbarian"
    FIGHTER = "Fighter"
    WIZARD = "Wizard"
    DRUID = "Druid"
    CLERIC = "Cleric"
    WARLOCK = "Warlock"
    MONK = "Monk"
    PALADIN = "Paladin"
    ROGUE = "Rogue"
    RANGER = "Ranger"
    SORCERER = "Sorcerer"
