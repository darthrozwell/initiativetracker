// src/components/Header.tsx

import SettingsIcon from "@mui/icons-material/Settings"
import SportsKabaddiIcon from "@mui/icons-material/SportsKabaddi"
import CloseIcon from "@mui/icons-material/Close"
import PlayArrowIcon from "@mui/icons-material/PlayArrow"
import RestartAltIcon from "@mui/icons-material/RestartAlt"

import { useNavigate } from "react-router-dom"

import {
    AppBar,
    Box, Button,
    IconButton,
    Toolbar, Tooltip,
    Typography,
} from "@mui/material"

interface HeaderProps {
    encounterName: string
    round: number
    combatStarted: boolean
    onResetCombat?: () => void
    onStartCombat?: () => void
}

export default function Header({
    encounterName,
    round,
    combatStarted,
    onResetCombat,
    onStartCombat,
}: HeaderProps) {
    const navigate = useNavigate()

    function renderCombatStatus() {
        if (combatStarted) {
            return (
                <>
                    <Typography
                        variant="caption"
                        color="text.secondary"
                    >
                        Раунд
                    </Typography>

                    <Typography
                        variant="h5"
                        color="primary"
                    >
                        {round}
                    </Typography>
                </>
            );
        }

        return (
            <Button
                variant="contained"
                size="large"
                endIcon={<PlayArrowIcon />}
                onClick={onStartCombat}
            >
                Start Combat
            </Button>
        );
    }

    return (
        <AppBar position="static">
            <Toolbar
                sx={{
                    display: "flex",
                    justifyContent: "space-between",
                    gap: 2,
                    px: 3,
                    minHeight: 64,
                }}
            >
                {/* Левая часть */}

                <Box
                    display="flex"
                    alignItems="center"
                    gap={2}
                >
                    <SportsKabaddiIcon
                        color="primary"
                        sx={{ fontSize: 30 }}
                    />

                    <Box>
                        <Typography
                            variant="h6"
                            lineHeight={1.1}
                        >
                            {encounterName}
                        </Typography>
                    </Box>
                </Box>

                {/* Центр */}

                <Box textAlign="center">
                    {renderCombatStatus()}
                </Box>

                {/* Правая часть */}

                <Box display="flex" alignItems="center">

                    <Tooltip title="Reset combat">
                        <IconButton
                            color="inherit"
                            size="large"
                            onClick={onResetCombat}
                        >
                            <RestartAltIcon />
                        </IconButton>
                    </Tooltip>

                    <IconButton
                        color="inherit"
                        size="large"
                    >
                        <SettingsIcon />
                    </IconButton>

                    <IconButton
                        color="error"
                        size="large"
                        aria-label="Close and go to encounters"
                        onClick={() => navigate('/')}
                    >
                        <CloseIcon />
                    </IconButton>
                </Box>
            </Toolbar>
        </AppBar>
    );
}