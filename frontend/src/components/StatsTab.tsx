// src/components/StatsTab.tsx

import {
    Grid,
    Paper,
    Typography,
} from "@mui/material";

import type {Attack, Combatant} from "../types/combat"
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
                                roll={combatant.strength_mod}
                                save={combatant.strength_save}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Ловкость"
                                roll={combatant.dexterity_mod}
                                save={combatant.dexterity_save}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Телосложение"
                                roll={combatant.constitution_mod}
                                save={combatant.constitution_save}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>
                        <Grid size={4}>
                            <BaseStatsCard
                                title="Интеллект"
                                roll={combatant.intelligence_mod}
                                save={combatant.intelligence_save}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Мудрость"
                                roll={combatant.wisdom_mod}
                                save={combatant.wisdom_save}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>

                        <Grid size={4}>
                            <BaseStatsCard
                                title="Харизма"
                                roll={combatant.charisma_mod}
                                save={combatant.charisma_save}
                                onRoll={(bonus: number) => onRoll(combatant, bonus)}
                            />
                        </Grid>
                    </Grid>

                    <Grid container spacing={0} pt={1}>
                        <Grid size={12}>
                        <DmgResStatCard
                                title={"Сопротивление урону"}
                                value={combatant.damage_resistance}
                            />
                        </Grid>

                        <Grid size={12}>
                        <DmgResStatCard
                                title={"Иммунитет к урону"}
                                value={combatant.damage_immunity}
                            />
                        </Grid>

                        <Grid size={12}>
                        <DmgResStatCard
                                title={"Уязвимость к урону"}
                                value={combatant.damage_vulnerability}
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

                    {combatant.abilities?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.abilities.filter((ability) => ability.title === "Особенности").map((attack: Attack, index: number) => (
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

                    {combatant.abilities?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.abilities.filter((ability) => ability.title === "Действия").map((attack: Attack, index: number) => (
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

                    {combatant.abilities?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.abilities.filter((ability) => ability.title === "Бонусные действия").map((attack: Attack, index: number) => (
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

                    {combatant.abilities?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.abilities.filter((ability) => ability.title === "Реакции").map((attack: Attack, index: number) => (
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

                    {combatant.abilities?.length > 0 && (
                          <Grid container spacing={0}>
                            {combatant.abilities.filter((ability) => ability.title === "Легендарные действия").map((attack: Attack, index: number) => (
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
