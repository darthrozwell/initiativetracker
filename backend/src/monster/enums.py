from enum import StrEnum


class MonsterSource(StrEnum):
    ADV_IN_FAERUN = "Forgotten Realms: Adventures in Faerun"
    BOOK_OF_HUNGERS = "Astarion's Book of Hungers"
    CUSTOM = "Custom"
    LORWYN = "Lorwyn: First Light"
    MM_2024 = "Monster Manual 2024"
    NETHERIL = "Netheril's Fall"
    PHB_2024 = "Player's Handbook 2024"
    RAVENLOFT = "Ravenloft: The Horrors Within"


class MonsterSize(StrEnum):
    TINY = "Крошечный"
    SMALL = "Маленький"
    AVG = "Средний"
    BIG = "Большой"
    HUGE = "Огромный"
    GIANT = "Громадный"


class MonsterType(StrEnum):
    ABERRATION = "Аберрация"
    BEAST = "Зверь"
    CELESTIAL = "Небожитель"
    CONSTRUCT = "Конструкт"
    DRAGON = "Дракон"
    ELEMENTAL = "Элементаль"
    FEY = "Фея"
    FIEND = "Исчадие"
    GIANT = "Великан"
    HUMANOID = "Гуманоид"
    MONSTROSITY = "Чудовище"
    OOZE = "Слизь"
    PLANT = "Растение"
    UNDEAD = "Нежить"
