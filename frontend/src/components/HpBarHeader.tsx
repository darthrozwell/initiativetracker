import { Box, Button, Stack, Typography, LinearProgress } from "@mui/material";

interface HpBarHeaderProps {
    current: number;
    max: number;
    onChange?: (delta: number) => void;
}

export default function HpBarHeader({
    current,
    max,
    onChange,
}: HpBarHeaderProps) {
    const percent = Math.max(0, Math.min(100, current / Math.max(max, 1) * 100));
    const getColor = () => {
        if (percent <= 25) return "#D64545";
        if (percent <= 50) return "#F0B429";
        return "#4CAF50";
    };

    return (
        <Box width="100%">
            <Box
                display="flex"
                alignItems="center"
                gap={2}
            >
                <Typography
                    variant="body2"
                    sx={{ width: 28 }}
                >
                    HP
                </Typography>

                <LinearProgress
                    variant="determinate"
                    value={percent}
                    sx={{
                        flex: 1,
                        height: 14,
                        borderRadius: 999,
                        bgcolor: "rgba(255,255,255,.08)",

                        "& .MuiLinearProgress-bar": {
                            backgroundColor: getColor(),
                            transition:
                                "transform 250ms ease, background-color 250ms ease",
                        },
                    }}
                />

                <Typography
                    sx={{
                        width: 100,
                        textAlign: "right",
                    }}
                >
                    {current} / {max}
                </Typography>
            </Box>

            <Stack
                direction="row"
                spacing={1}
                mt={2}
            >
                {[-10, -5, -1, 1, 5, 10].map(v => (
                    <Button
                        key={v}
                        variant="outlined"
                        size="small"
                        color={v < 0 ? "error" : "success"}
                        sx={{
                            minWidth: 64,
                            flex: 1,
                        }}
                        onClick={() => onChange?.(v)}
                    >
                        {v > 0 ? `+${v}` : v}
                    </Button>
                ))}
            </Stack>
        </Box>
    );
}