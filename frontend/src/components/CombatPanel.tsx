// src/components/CombatPanel.tsx

import {
    Avatar,
    Box,
    Chip,
    Paper,
    Tab,
    Tabs,
    Typography,
} from "@mui/material";
import { useState } from "react";

import type {Combatant, HistoryEntry} from "../types/combat";
import HpBarHeader from "./HpBarHeader.tsx"
import StatsTab from "./StatsTab";
import EffectsTab from "./EffectsTab";
import HistoryTab from "./HistoryTab";

interface CombatPanelProps {
    combatant?: Combatant | null
    history?: HistoryEntry[]
    onHpChange?: (combatant: Combatant, delta: number) => void
    onStatRoll?: (comb: Combatant, bonus: number) => void
    onUpdateCombatant?: (comb_id: string, changes: Partial<Combatant>) => void
}

export default function CombatPanel({
    combatant = null,
    history = [],
    onHpChange,
    onStatRoll,
    onUpdateCombatant,
}: CombatPanelProps) {
    const [tab, setTab] = useState(0)


    // Если нет переданного комбатанта — показываем пустой макет
    if (!combatant) {
        return (
            <Paper
                square
                sx={{
                    flex: 1,
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    justifyContent: "center",
                    p: 4,
                }}
            >
                <Typography variant="h6" color="text.secondary">
                    No combatant selected
                </Typography>
            </Paper>
        );
    }

    return (
        <Paper
            square
            sx={{
                flex: 1,
                height: "100%",
                display: "flex",
                flexDirection: "column",
            }}
        >
            {/* ---------- HEADER ---------- */}

            <Box sx={{
                    borderBottom: "1px solid",
                    borderColor: "divider",
                }}
                 p={1}>

                <Box
                    display="flex"
                    justifyContent="space-between"
                    alignItems="flex-start"
                    gap={5}
                >
                    <Box
                        display="flex"
                        gap={3}
                        alignItems="center"
                        flex={1}
                    >
                        <Avatar
                            src={combatant.portrait}
                            sx={{
                                width: 64,
                                height: 64,
                                fontSize: 24,
                            }}
                        >
                            {combatant.name?.charAt(0)}
                        </Avatar>

                        <Box>
                            <Typography variant="h5">
                                {combatant.name}
                            </Typography>

                            <Box display="flex" alignItems="center" gap={5} mt={0.5}>
                                <Typography variant={"caption"} color="text.secondary">
                                    {combatant.type === "monster"
                                        ? combatant.creature_type
                                        : combatant.character_class}
                                </Typography>

                                <Chip
                                    size="small"
                                    label={combatant.status}
                                    color={
                                        combatant.status === "dead"
                                            ? "error"
                                            : combatant.status === "unconscious"
                                            ? "warning"
                                            : "success"
                                    }
                                />
                              </Box>
                        </Box>
                    </Box>

                    <Box
                        sx={{
                            width: 580,
                            maxWidth: "45%",
                        }}
                    >
                        <HpBarHeader
                            current={combatant.current_hp}
                            max={combatant.hit_points_value}
                            onChange={(delta) =>
                                    onHpChange?.(combatant, delta)
                            }
                        />
                    </Box>
                </Box>
                <Box mt={0}
                >
                    <Tabs
                        // centered
                        // orientation="vertical"
                        value={tab}
                        onChange={(_, value) => setTab(value)}
                    >
                        <Tab label="Statistics" />
                        <Tab label="Effects" />
                        <Tab label="History" />
                    </Tabs>
                </Box>
            </Box>



            {/* ---------- CONTENT ---------- */}

            <Box
                sx={{
                    flex: 1,
                    overflow: "auto",
                    p: 2,
                }}
            >
                {tab === 0 && (
                    <StatsTab
                        combatant={combatant}
                        onRoll={(comb: Combatant, bonus: number) => onStatRoll(comb, bonus)}
                        onUpdate={(changes) =>
                                    onUpdateCombatant(combatant.combatant_id, changes)
                                }
                    />
                )}

                {tab === 1 && (
                    <EffectsTab
                        effects={[]}
                    />
                )}

                {tab === 2 && (
                    <HistoryTab history={history ?? []} />
                )}
            </Box>
        </Paper>
    );
}