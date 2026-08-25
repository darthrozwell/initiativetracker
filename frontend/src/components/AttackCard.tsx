// src/components/StatCard.tsx

import {
    Grid,
    Paper,
    Typography,
} from "@mui/material"
import type {Action} from "../types/combat.ts"

interface AttackCardProps {
    attack: Action
}

export default function AttackCard({
    attack,
}: AttackCardProps) {
    return (
        <Paper
            sx={{
                p: 1,
                height: "100%",
                display: "flex",
                flexDirection: "column",
                justifyContent: "left",
                alignItems: "left",
                textAlign: "left",
            }}
        >
            <Grid container>
                <Grid size={12}>
                    <Typography
                        variant="subtitle1"
                        color="text.primary"
                        sx={{
                            p: 0.5,
                            letterSpacing: 1,
                        }}
                    >
                        {attack.name? attack.name: "attack"}
                    </Typography>
                </Grid>

                <Grid size={12}>
                    <Typography
                        variant="body2"
                        sx={{
                            mt: 0,
                            p: 0.5,
                            fontWeight: 580,
                            lineHeight: 1.2,
                        }}
                    >
                        {attack.text? attack.text: "text"}
                    </Typography>
                </Grid>
            </Grid>
        </Paper>
    )
}