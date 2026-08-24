// src/components/StatCard.tsx

import {
    Grid,
    Paper,
    Typography,
} from "@mui/material"

interface DmgResCardProps {
    title: string
    value: string
}

export default function DmgResStatCard({
    title,
    value,
}: DmgResCardProps) {
    return (
        <Paper
            sx={{
                p: 0.5,
                height: "100%",
                display: "flex",
                flexDirection: "column",
                justifyContent: "left",
                textAlign: "left",
            }}
        >
            <Grid container>
                <Grid size={4}>
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

                <Grid size={8}>
                    <Typography
                        variant="subtitle1"
                        sx={{
                            p: 0.5,
                            fontWeight: 580,
                            lineHeight: 1.2,
                        }}
                    >
                        {value}
                    </Typography>
                </Grid>
            </Grid>
        </Paper>
    );
}