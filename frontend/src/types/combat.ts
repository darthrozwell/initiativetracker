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


export interface Effect {
    id: number
    name: string
    duration: number | null
    color?: string
}

export interface Attack {
    title: string
    name: string
    text: string
    attack_type: string
    attack_range: string
    hit_bonus: number
    reach: string
    damage: string
}


export interface Creature {
    name: string
    source: string

    armor_class: number
    initiative: number
    hit_points_value: number
    speed: string
    damage_resistance?: string
    damage_immunity?: string
    damage_vulnerability?: string

    strength_value: number
    strength_mod: number
    strength_save: number
    dexterity_value: number
    dexterity_mod: number
    dexterity_save: number
    constitution_value: number
    constitution_mod: number
    constitution_save: number
    intelligence_value: number
    intelligence_mod: number
    intelligence_save: number
    wisdom_value: number
    wisdom_mod: number
    wisdom_save: number
    charisma_value: number
    charisma_mod: number
    charisma_save: number

    abilities?: Attack[]
}


export interface Monster extends Creature {
    monster_id: string
    size: MonsterSize
    creature_type: MonsterType
    alignment: MonsterAlignment

    hit_points_formula: string
    skills?: string
    senses?: string
    languages?: string
    challenge_rating: string
    experience: number
    proficiency_bonus: number
    equipment?: string
    treasure?: string
    habitat?: string
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
