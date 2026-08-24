// src/components/EffectsTab.tsx

import {
    Box,
    Chip,
    Paper,
    Stack,
    Typography,
} from "@mui/material";

import type {Effect} from "../types/combat";

interface EffectsTabProps {
    effects: Effect[];
}

export default function EffectsTab({
    effects,
}: EffectsTabProps) {
    if (effects.length === 0) {
        return (
            <Box
                display="flex"
                justifyContent="center"
                alignItems="center"
                height="100%"
            >
                <Typography color="text.secondary">
                    No active effects
                </Typography>
            </Box>
        );
    }

    return (
        <Stack spacing={2}>
            {effects.map((effect) => (
                <Paper
                    key={effect.id}
                    sx={{
                        p: 2,
                    }}
                >
                    <Box
                        display="flex"
                        justifyContent="space-between"
                        alignItems="center"
                    >
                        <Typography variant="subtitle1">
                            {effect.name}
                        </Typography>

                        <Chip
                            size="small"
                            color="primary"
                            label={
                                effect.duration === null
                                    ? "Permanent"
                                    : `${effect.duration} rounds`
                            }
                        />
                    </Box>

                    <Typography
                        mt={1}
                        variant="body2"
                        color="text.secondary"
                    >
                        {effect.duration === null
                            ? "This effect has no duration."
                            : `Remaining duration: ${effect.duration} rounds.`}
                    </Typography>
                </Paper>
            ))}
        </Stack>
    );
}