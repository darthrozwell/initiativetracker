// src/components/HistoryTab.tsx

import {
    Box,
    Paper,
    Stack,
    Typography,
} from "@mui/material";

import type {HistoryEntry} from "../types/combat";

interface HistoryTabProps {
    history: HistoryEntry[];
}

export default function HistoryTab({
    history,
}: HistoryTabProps) {
    if (history.length === 0) {
        return (
            <Box
                display="flex"
                justifyContent="center"
                alignItems="center"
                height="100%"
            >
                <Typography color="text.secondary">
                    No actions have been recorded.
                </Typography>
            </Box>
        );
    }

    return (
        <Stack spacing={2}>
            {history.map((entry) => (
                <Paper
                    key={entry.id}
                    sx={{
                        p: 2,
                    }}
                >
                    <Box
                        display="flex"
                        justifyContent="space-between"
                        alignItems="center"
                    >
                        <Typography variant="subtitle2">
                            Round {entry.round}
                        </Typography>

                        <Typography
                            variant="caption"
                            color="text.secondary"
                        >
                            {entry.timestamp}
                        </Typography>
                    </Box>

                    <Typography
                        mt={1}
                        variant="body1"
                    >
                        {entry.text}
                    </Typography>
                </Paper>
            ))}
        </Stack>
    );
}