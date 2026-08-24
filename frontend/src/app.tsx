import { CssBaseline, ThemeProvider } from "@mui/material";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { theme } from "./theme";
import CombatPage from "./pages/CombatPage";
import EncounterList from "./pages/EncounterList";

export default function App() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />

            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<EncounterList />} />
                    <Route path="/encounter/:id" element={<CombatPage />} />
                </Routes>
            </BrowserRouter>
        </ThemeProvider>
    );
}