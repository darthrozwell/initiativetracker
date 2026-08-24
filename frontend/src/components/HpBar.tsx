// src/components/HpBar.tsx

import { Box, LinearProgress, Typography } from "@mui/material";

interface HpBarProps {
    current: number;
    max: number;
    height?: number;
    showPercent?: boolean;
}

export default function HpBar({
    current,
    max,
    height = 10,
    showPercent = false,
}: HpBarProps) {
    const hp = Math.max(0, current);
    const maximum = Math.max(1, max);

    const percent = Math.min((hp / maximum) * 100, 100);

    const getColor = () => {
        if (percent <= 25) return "#D64545";
        if (percent <= 50) return "#F0B429";
        return "#4CAF50";
    };

    return (
        <Box width="100%">
            <LinearProgress
                variant="determinate"
                value={percent}
                sx={{
                    height,
                    borderRadius: 999,

                    "& .MuiLinearProgress-bar": {
                        backgroundColor: getColor(),
                        transition:
                            "transform 250ms ease, background-color 250ms ease",
                    },
                }}
            />

            {showPercent && (
                <Typography
                    mt={0.5}
                    variant="caption"
                    color="text.secondary"
                    align="right"
                    display="block"
                >
                    {Math.round(percent)}%
                </Typography>
            )}
        </Box>
    );
}