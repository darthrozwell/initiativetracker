// src/components/StatCard.tsx

import {
    Box,
    Button,
    Grid,
    Paper,
    Typography,
} from "@mui/material"
import rolld20 from "../assets/rolld20.png"

interface BaseStatCardProps {
    title: string
    roll: number
    save: number
    onRoll?: (bonus: number) => void
}

export default function BaseStatCard({
    title,
    roll,
    save,
    onRoll,
}: BaseStatCardProps) {
    return (
        <Paper
            sx={{
                p: 0.5,
                height: "100%",
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
                alignItems: "left",
                textAlign: "center",
            }}
        >
            <Grid
                container
                spacing={1}
                sx={{
                    justifyContent: "space-between",
                    alignItems: "center",
                  }}>
                <Grid size={12}>
                    <Typography
                        variant="caption"
                        color="text.secondary"
                        sx={{
                            p: 0.5,
                            textTransform: "uppercase",
                            letterSpacing: 1,
                        }}
                    >
                        {title}
                    </Typography>
                </Grid>
                <Grid size={6}>
                    <Button
                        onClick={() => onRoll(roll)}
                        sx={{
                            position: "relative",
                            minWidth: 0,
                            padding: 0,
                        }}
                    >
                        <Box
                            component="img"
                            src={rolld20}
                            alt="Roll D20"
                            sx={{
                                width: 80,
                                height: 80,
                                display: "block",
                            }}
                        />

                        <Typography
                            sx={{
                                position: "absolute",
                                top: "50%",
                                left: "50%",
                                transform: "translate(-50%, -50%)",
                                color: "white",
                                fontWeight: 580,
                                fontSize: 20,
                            }}
                        >
                            {roll}
                        </Typography>

                    </Button>

                </Grid>

                <Grid size={6}>
                    <Button
                        onClick={() => onRoll(save)}
                        sx={{
                            position: "relative",
                            minWidth: 0,
                            padding: 0,
                        }}
                    >
                        <Box
                            component="img"
                            src={rolld20}
                            alt="Roll D20"
                            sx={{
                                width: 80,
                                height: 80,
                                display: "block",
                            }}
                        />

                        <Typography
                            sx={{
                                position: "absolute",
                                top: "50%",
                                left: "50%",
                                transform: "translate(-50%, -50%)",
                                color: "white",
                                fontWeight: 580,
                                fontSize: 20,
                            }}
                        >
                            {save}
                        </Typography>

                    </Button>

                </Grid>
            </Grid>
        </Paper>
    );
}