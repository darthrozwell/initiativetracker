// src/components/Footer.tsx

import ArrowBackIcon from "@mui/icons-material/ArrowBack"
import ArrowForwardIcon from "@mui/icons-material/ArrowForward"
import StopCircleIcon from "@mui/icons-material/StopCircle"

import {
    Button,
    Paper,
} from "@mui/material"

interface FooterProps {
    combatStarted: boolean
    onPrevious?: () => void
    onNext?: () => void
    onEndCombat?: () => void
}

export default function Footer({
    combatStarted,
    onPrevious,
    onNext,
    onEndCombat,
}: FooterProps) {
    return (
        <Paper
            square
            sx={{
                height: 72,
                px: 3,
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                borderTop: 1,
                borderColor: "divider",
            }}
        >
            <Button
                variant="outlined"
                size="large"
                startIcon={<ArrowBackIcon />}
                onClick={onPrevious}
                disabled={!combatStarted}
            >
                Previous
            </Button>

            <Button
                variant="contained"
                size="large"
                endIcon={<ArrowForwardIcon />}
                onClick={onNext}
                disabled={!combatStarted}
            >
                Next Turn
            </Button>

            <Button
                variant="outlined"
                color="error"
                size="large"
                startIcon={<StopCircleIcon />}
                onClick={onEndCombat}
                disabled={!combatStarted}
            >
                End Combat
            </Button>
        </Paper>
    );
}