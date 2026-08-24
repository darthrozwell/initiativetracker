import { Alert, Snackbar } from "@mui/material"

interface RollSnackbarProps {
    open: boolean
    actor: string
    formula: string
    roll_result: number
    bonus: number
    onClose: () => void
}

export default function RollSnackbar({
    open,
    actor,
    formula,
    roll_result,
    bonus,
    onClose,
}: RollSnackbarProps) {
    return (
        <Snackbar
            open={open}
            autoHideDuration={4000}
            onClose={onClose}
            anchorOrigin={{
                vertical: "top",
                horizontal: "center",
            }}
            // sx={{
            //     bottom: 188,
            // }}
        >
            <Alert
                onClose={onClose}
                severity={
                    roll_result === 20
                        ? "success"
                        : roll_result === 1
                            ? "error"
                            : "info"
                }
                variant="filled"
            >
                {actor} — {formula} → {Math.max(roll_result + bonus, 1)}
            </Alert>
        </Snackbar>
    )
}