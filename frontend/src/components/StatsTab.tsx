// src/components/StatsTab.tsx

import {
    Grid,
    Paper,
    Typography,
} from "@mui/material";

import type {Action, Combatant} from "../types/combat"
import StatCard from "./StatCard"
import BaseStatsCard from "./BasestatsCard.tsx"
import DmgResStatCard from "./DmgResCard.tsx"
import AttackCard from "./AttackCard.tsx"

interface StatsTabProps {
    combatant: Combatant
    onRoll: (comb: Combatant, bonus: number) => void
    onUpdate: (
        changes: Partial<Combatant>
    ) => void
}

export default function StatsTab({
    combatant,
    onRoll,
    onUpdate,
}: StatsTabProps) {
    return (
        <Grid
            container
            direction="row"
            spacing={1}
        >
            {/* Основные характеристики */}



            {/* Общая информация */}
            <Grid size={6}>
                <Paper sx={{ p: 2 }}>
                    <Grid container spacing={1} p={0}>

                        <Grid size={4}>
                            <StatCard
                                title="Класс Защиты"
                                value={combatant.armor_class}
                            />
                        </Grid>

                        <Grid size={4}>
                            <StatCard
                                title="Скорость"
                                value={combatant.speed}
                            />
                        </Grid>

                        <Grid size={4}>
                            <StatCard
                                title="Инициатива"
                                value={combatant.current_initiative}
                                editable
                                onChange={(value) =>
                                            onUpdate({
                                                current_initiative: value,
                                            })
    }
                            />
                        </Grid>
                    </Grid>

                    <Grid container spacing={1} pt={1}>
                        <Grid size={4}>
                            <BaseStatsCard
                                title="Сила"
                                roll={Math.floor((combatant.strength_value - 10) / 2)}
                                save={Math.floor((combatant.strength_value - 10) / 2) + (combatant.is_strength_save ? combatant.proficiency_bonus : 0)}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Ловкость"
                                roll={Math.floor((combatant.dexterity_value - 10) / 2)}
                                save={Math.floor((combatant.dexterity_value - 10) / 2) + (combatant.is_dexterity_save ? combatant.proficiency_bonus : 0)}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Телосложение"
                                roll={Math.floor((combatant.constitution_value - 10) / 2)}
                                save={Math.floor((combatant.constitution_value - 10) / 2) + (combatant.is_constitution_save ? combatant.proficiency_bonus : 0)}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>
                        <Grid size={4}>
                            <BaseStatsCard
                                title="Интеллект"
                                roll={Math.floor((combatant.intelligence_value - 10) / 2)}
                                save={Math.floor((combatant.intelligence_value - 10) / 2) + (combatant.is_intelligence_save ? combatant.proficiency_bonus : 0)}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Мудрость"
                                roll={Math.floor((combatant.wisdom_value - 10) / 2)}
                                save={Math.floor((combatant.wisdom_value - 10) / 2) + (combatant.is_wisdom_save ? combatant.proficiency_bonus : 0)}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Харизма"
                                roll={Math.floor((combatant.charisma_value - 10) / 2)}
                                save={Math.floor((combatant.charisma_value - 10) / 2) + (combatant.is_charisma_save ? combatant.proficiency_bonus : 0)}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>
                    </Grid>

                    <Grid container spacing={0} pt={1}>
                        <Grid size={12}>
                        <DmgResStatCard
                                title={"Сопротивление урону"}
                                value={combatant.protections.damage_resistance}
                            />
                        </Grid>

                        <Grid size={12}>
                        <DmgResStatCard
                                title={"Иммунитет к урону"}
                                value={combatant.protections.damage_immunity}
                            />
                        </Grid>

                        <Grid size={12}>
                        <DmgResStatCard
                                title={"Уязвимость к урону"}
                                value={combatant.protections.damage_vulnerability}
                            />
                        </Grid>
                    </Grid>

                </Paper>
            </Grid>

                {/* Заметки */}

            <Grid size={6}>
                <Paper sx={{ p: 1 }}>
                    <Typography
                        variant="h6"
                        gutterBottom
                        sx={{
                            p: 0.5,
                            letterSpacing: 1,
                        }}
                    >
                        Особенности
                    </Typography>

                    {combatant.actions?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.actions.filter((ability) => ability.type === "Особенности").map((attack: Action, index: number) => (
                              <Grid key={index}>
                                <AttackCard attack={attack} />
                              </Grid>
                            ))}
                          </Grid>
                        )}

                    <Typography
                        variant="h6"
                        gutterBottom
                        sx={{
                            p: 0.5,
                            letterSpacing: 1,
                        }}
                    >
                        Действия
                    </Typography>

                    {combatant.actions?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.actions.filter((ability) => ability.type === "Действия").map((attack: Action, index: number) => (
                              <Grid key={index}>
                                <AttackCard attack={attack} />
                              </Grid>
                            ))}
                          </Grid>
                        )}

                    <Typography
                        variant="h6"
                        gutterBottom
                        sx={{
                            p: 0.5,
                            letterSpacing: 1,
                        }}
                    >
                        Бонусные действия
                    </Typography>

                    {combatant.actions?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.actions.filter((ability) => ability.type === "Бонусные действия").map((attack: Action, index: number) => (
                              <Grid key={index}>
                                <AttackCard attack={attack} />
                              </Grid>
                            ))}
                          </Grid>
                        )}

                    <Typography
                        variant="h6"
                        gutterBottom
                        sx={{
                            p: 0.5,
                            letterSpacing: 1,
                        }}
                    >
                        Реакции
                    </Typography>

                    {combatant.actions?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.actions.filter((ability) => ability.type === "Реакции").map((attack: Action, index: number) => (
                              <Grid key={index}>
                                <AttackCard attack={attack} />
                              </Grid>
                            ))}
                          </Grid>
                        )}

                    <Typography
                        variant="h6"
                        gutterBottom
                        sx={{
                            p: 0.5,
                            letterSpacing: 1,
                        }}
                    >
                        Легендарные действия
                    </Typography>

                    {combatant.actions?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.actions.filter((ability) => ability.type === "Легендарные действия").map((attack: Action, index: number) => (
                              <Grid key={index}>
                                <AttackCard attack={attack} />
                              </Grid>
                            ))}
                          </Grid>
                        )}

                </Paper>
            </Grid>
        </Grid>
    );
}
