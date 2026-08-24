// src/components/InitiativeCard.tsx

import PersonIcon from "@mui/icons-material/Person";
import ShieldIcon from "@mui/icons-material/Shield";
import SmartToyIcon from "@mui/icons-material/SmartToy";
import StarIcon from "@mui/icons-material/Star";
import CloseIcon from "@mui/icons-material/Close";

import {
    Avatar,
    Box,
    Chip,
    Paper,
    Typography,
    IconButton,
} from "@mui/material";

import type {Combatant} from "../types/combat";
import HpBar from "./HpBar";

interface InitiativeCardProps {
    combatant: Combatant;
    selected: boolean;
    active_turn: boolean;
    onClick: () => void;
    onDelete?: () => void;
}

export default function InitiativeCard({
    combatant,
    selected,
    active_turn,
    onClick,
    onDelete,
}: InitiativeCardProps) {

    const avatarIcon =
        combatant.type === "monster" ? (
            <SmartToyIcon />
        ) : (
            <PersonIcon />
        );

    return (
        <Paper
            onClick={onClick}
            sx={{
                cursor: "pointer",
                p: 2,
                transition: "all .15s ease",

                opacity: combatant.status === "dead" || combatant.status === "unconscious" ? 0.5 : 1,

                borderColor: selected
                    ? "primary.main"
                    : "divider",

                borderWidth: selected ? 2 : 1,

                "&:hover": {
                    transform: "translateY(-2px)",
                    borderColor: "primary.main",
                },
            }}
        >
            {/* Верхняя строка */}

            <Box
                display="flex"
                alignItems="center"
                justifyContent="space-between"
            >
                <Chip
                    label={combatant.current_initiative}
                    color={active_turn ? "primary" : "default"}
                    size="small"
                />

                <Box display="flex" gap={0.5} alignItems="center">
                    {active_turn && (
                        <StarIcon
                            color="primary"
                            fontSize="small"
                        />
                    )}
                    {onDelete && (
                        <IconButton
                            size="small"
                            color="error"
                            onClick={(e) => {
                                e.stopPropagation();
                                onDelete();
                            }}
                        >
                            <CloseIcon fontSize="small" />
                        </IconButton>
                    )}
                </Box>
            </Box>

            {/* Имя */}

            <Box
                mt={1.5}
                display="flex"
                gap={1.5}
                alignItems="center"
            >
                <Avatar
                    src={combatant.portrait}
                    sx={{
                        width: 42,
                        height: 42,
                    }}
                >
                    {avatarIcon}
                </Avatar>

                <Box
                    sx={{
                        flex: 1,
                        minWidth: 0,
                    }}
                >
                    <Typography
                        variant="subtitle1"
                        noWrap
                    >
                        {combatant.nickname}
                    </Typography>
                </Box>
            </Box>

            {/* HP */}

            <Box mt={2}>
                <HpBar
                    current={combatant.current_hp}
                    max={combatant.hit_points_value}
                />

                <Box
                    mt={0.5}
                    display="flex"
                    justifyContent="space-between"
                >
                    <Typography variant="caption">
                        HP
                    </Typography>

                    <Typography
                        variant="caption"
                    >
                        {combatant.current_hp} / {combatant.hit_points_value}
                    </Typography>
                </Box>
            </Box>

            {/* Нижняя строка */}

            <Box
                mt={2}
                display="flex"
                justifyContent="space-between"
                alignItems="center"
            >
                <Box
                    display="flex"
                    alignItems="center"
                    gap={0.5}
                >
                    <ShieldIcon
                        sx={{
                            fontSize: 16,
                            color: "text.secondary",
                        }}
                    />

                    <Typography variant="caption">
                        {combatant.armor_class}
                    </Typography>
                </Box>

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
        </Paper>
    );
}