// src/types/combat.ts


export type CombatantType = "character" | "monster" | "npc"

export type CombatantStatus =
    | "alive"
    | "unconscious"
    | "dead"

export type Race =
    | "Aasimar"
    | "Gnome"
    | "Goliath"
    | "Dwarf"
    | "Dragonborn"
    | "Orc"
    | "Halfling"
    | "Tiefling"
    | "Human"
    | "Elf"

export type CharacterClass =
    | "Artificer"
    | "Bard"
    | "Barbarian"
    | "Fighter"
    | "Wizard"
    | "Druid"
    | "Cleric"
    | "Warlock"
    | "Monk"
    | "Paladin"
    | "Rogue"
    | "Ranger"
    | "Sorcerer"

export type MonsterSize =
    | "Крошечный"
    | "Маленький"
    | "Средний"
    | "Большой"
    | "Огромный"
    | "Громадный"

export type MonsterAlignment =
    | "Хаотичный Злой"
    | "Хаотичный Нейтральный"
    | "Хаотичный Добрый"
    | "Нейтральный Злой"
    | "Нейтральный"
    | "Нейтральный Добрый"
    | "Принципиальный Злой"
    | "Принципиальный Нейтральный"
    | "Принципиальный Добрый"

export type MonsterType =
    | "Аберрация"
    | "Зверь"
    | "Небожитель"
    | "Конструкт"
    | "Дракон"
    | "Элементаль"
    | "Фея"
    | "Исчадие"
    | "Великан"
    | "Гуманоид"
    | "Чудовище"
    | "Слизь"
    | "Растение"
    | "Нежить"

export type ActionType =
    | "Действия"
    | "Бонусные действия"
    | "Реакции"
    | "Легендарные действия"
    | "Особенности"

export type DamageType =
    | "Дробящий"
    | "Колющий"
    | "Рубящий"
    | "Кислота"
    | "Холод"
    | "Огонь"
    | "Силовой"
    | "Электричество"
    | "Некротический"
    | "Яд"
    | "Психический"
    | "Излучение"
    | "Звук"


export interface Damage {
    damage: string
    damage_type: DamageType
}

export interface Effect {
    id: number
    name: string
    duration: number | null
    color?: string
}

export interface Action {
    type: ActionType
    name: string
    text: string
    range: string
    reach: string
    hit_bonus: number
    damage: Damage[]
}


export interface Creature {
    name: string
    source: string
    alignment: MonsterAlignment

    armor_class: number
    initiative: number
    hit_points_value: number
    speed: string

    protections: {
        damage_resistance: DamageType[]
        damage_immunity: DamageType[]
        damage_vulnerability: DamageType[]
    }

    skills: string
    senses: string
    languages: string
    proficiency_bonus: number

    strength_value: number
    is_strength_save: boolean
    dexterity_value: number
    is_dexterity_save: boolean
    constitution_value: number
    is_constitution_save: boolean
    intelligence_value: number
    is_intelligence_save: boolean
    wisdom_value: number
    is_wisdom_save: boolean
    charisma_value: number
    is_charisma_save: boolean

    actions: Action[]
}


export interface Monster extends Creature {
    monster_id: string
    size: MonsterSize
    creature_type: MonsterType

    hit_points_formula: string
    skills: string
    senses: string
    languages: string
    challenge_rating: string
    experience: number
    proficiency_bonus: number
    equipment: string
    treasure: string
    habitat: string
}

export type MonsterCreationForm = Omit<
    Monster,
    | "monster_id"
>


export interface Character extends Creature {
    character_id: string
    character_class: CharacterClass
    race: Race
}

export type CharacterCreationForm = Omit<
    Character,
    | "character_id"
>


export interface BaseCombatant {
    combatant_id: string
    nickname: string
    current_hp: number
    current_initiative: number
    status: CombatantStatus

    type: CombatantType
    portrait?: string
}

export interface MonsterCombatant extends Monster, BaseCombatant {
    type: "monster"
}
export interface CharacterCombatant extends Character, BaseCombatant {
    type: "character"
}
export type Combatant = MonsterCombatant | CharacterCombatant


export interface CombatantPayload {
    monster_id?: string | null
    character_id?: string | null
    nickname: string
    current_hp: number
    current_initiative: number
    status: CombatantStatus
}

export interface HistoryEntry {
    id: number
    round: number
    combatant_id: number
    text: string
    timestamp: string
}

export interface Encounter {
    encounter_id: string
    name: string
    round: number
    current_turn: number
    combatants: Combatant[]
    history: HistoryEntry[]
}
