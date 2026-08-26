// src/components/Sidebar.tsx

import AddIcon from "@mui/icons-material/Add"
import {
    Box,
    Button,
    Divider,
    Paper,
    Stack,
    Typography,
    Dialog,
    DialogContent,
    DialogActions,
    List,
    ListItemButton,
    ListItemText,
    CircularProgress,
    Tooltip, Tab, Tabs, ListItem, IconButton, TextField
} from "@mui/material"
import {useEffect, useRef, useState} from "react"

import InitiativeCard from "./InitiativeCard"
import type {CharacterCombatant, Combatant, MonsterCombatant} from "../types/combat"
import {createMonster, getAllMonsters} from "../api/monster"
import rolld20 from "../assets/rolld20.png";
import CharacterForm from "./CreateCharacterTab.tsx";
import {createCharacter, deleteCharacter, getAllCharacters} from "../api/character.ts";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import MonsterForm from "./CreateMonsterTab.tsx";

interface SidebarProps {
    combatants?: Combatant[]
    selected_id?: number | null
    current_turn?: number | null

    onSelect?: (combatant_id: number | null) => void
    onAddCombatant?: (monster: any) => void
    onDeleteCombatant?: (combatant_id: number) => void
    onRerollInitiative?: () => void
}

export default function Sidebar({
    combatants = [],
    selected_id = null,
    current_turn = null,
    onSelect = () => {},
    onAddCombatant,
    onDeleteCombatant,
    onRerollInitiative,
}: SidebarProps) {
    const [openDialog, setOpenDialog] = useState(false)
    const [monsters, setMonsters] = useState<MonsterCombatant[]>([])
    const [characters, setCharacters] = useState<CharacterCombatant[]>([])
    const [loadingMonsters, setLoadingMonsters] = useState(false)
    const [dialogTab, setDialogTab] = useState(0)
    const [monsterSearch, setMonsterSearch] = useState("")

    async function handleAddClick() {
        setLoadingMonsters(true);
        try {
            setOpenDialog(true)
            const data = await getAllMonsters()
            setMonsters(data ?? []);
            const char_data = await getAllCharacters()
            setCharacters(char_data ?? [])
        } catch (err) {
            console.error("Failed to load monsters", err)
        } finally {
            setLoadingMonsters(false)
        }
    }

    function handleSelectCreature(creature: Combatant) {
        // monster.type = "monster"
        onAddCombatant?.(creature)
        setOpenDialog(false)
    }

    const handleUpdateCharacter = async () => {
        return
    }

    const handleDeleteCharacter = async (character_id: string) => {
        try {
            await deleteCharacter(character_id);

            setCharacters((prev) =>
                prev.filter(
                    (character) => character.character_id !== character_id
                )
            )
        } catch (error) {
            console.error("Failed to delete character:", error)
        }
    }

    const handleCreateCharacter = async (data) => {
        try {
            const response = await createCharacter(data)
            alert(response.character_id)
            setOpenDialog(false)
        } catch (error) {
            console.error("Failed to create character:", error)
        }
    }

    const handleCreateMonster = async (data) => {
        try {
            const response = await createMonster(data)
            alert(response.monster_id)
            setOpenDialog(false)
        } catch (error) {
            console.error("Failed to create monster:", error)
        }
    }

    const listRef = useRef<HTMLDivElement>(null)
    const combatantRefs = useRef<(HTMLDivElement | null)[]>([])

    useEffect(() => {
        if (selected_id === null) return
        const container = listRef.current
        const element = combatantRefs.current[selected_id]
        if (!container || !element) return

        container.scrollTo({
            top: element.offsetTop - container.offsetTop - 12,
            behavior: "smooth",
        })
    }, [selected_id, combatants])


    return (
        <>
            <Paper
                square
                sx={{
                    width: 320,
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                    borderRight: 1,
                    borderColor: "divider",
                }}
            >
                {/* Заголовок */}

                <Box
                    px={2}
                    py={2}
                    sx={{
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "space-between",
                    }}
                >
                    <Box>
                        <Typography variant="h6">
                            Initiative
                        </Typography>

                        <Typography
                            variant="body2"
                            color="text.secondary"
                        >
                            {combatants.length} participants
                        </Typography>
                    </Box>

                    <Box sx={{ display: "flex", gap: 0.5 }}>
                        <Tooltip title="Reroll all initiative">
                            <Button
                                onClick={onRerollInitiative}
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
                                        width: 60,
                                        height: 60,
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
                                    R
                                </Typography>

                            </Button>
                        </Tooltip>
                    </Box>
                </Box>

                <Divider />

                {/* Список участников */}

                <Stack
                    ref={listRef}
                    spacing={1.5}
                    sx={{
                        flex: 1,
                        overflowY: "auto",
                        p: 2,
                    }}
                >
                    {combatants.map((combatant: Combatant, index: number) => (
                        <Box
                            key={combatant.combatant_id}
                            ref={(element: HTMLDivElement | null) => {
                                combatantRefs.current[index] = element
                            }}
                        >
                        <InitiativeCard
                            key={index}
                            combatant={combatant}
                            selected={index === selected_id}
                            active_turn={current_turn !== null && index === current_turn}
                            onClick={() => onSelect?.(index)}
                            onDelete={() => onDeleteCombatant?.(index)}
                        />
                        </Box>
                    ))}
                </Stack>

                <Divider />

                {/* Кнопка добавления */}

                <Box p={2}>
                    <Button
                        fullWidth
                        variant="contained"
                        startIcon={<AddIcon />}
                        onClick={handleAddClick}
                        disabled={loadingMonsters}
                    >
                        Add Combatant
                    </Button>
                </Box>
            </Paper>

            {/* Dialog для выбора монстра */}
            <Dialog open={openDialog} onClose={() => setOpenDialog(false)} maxWidth="xl" fullWidth>
                <Box>
                    <Tabs
                        value={dialogTab}
                        onChange={(_, newValue) => setDialogTab(newValue)}
                        variant="fullWidth"
                    >
                        <Tab label="Добавить монстра"/>
                        <Tab label="Создать монстра" />
                        <Tab label="Добавить игрока" />
                        <Tab label="Создать игрока" />
                    </Tabs>
                </Box>
                <DialogContent>
                    {dialogTab === 0 && (
                        <Box sx={{ pt: 2 }}>
                            <TextField
                                fullWidth
                                size="small"
                                label="Search monster"
                                placeholder="Enter monster name..."
                                value={monsterSearch}
                                onChange={(e) => setMonsterSearch(e.target.value)}
                                sx={{ mb: 2 }}
                            />

                            {loadingMonsters ? (
                                <Box sx={{ display: "flex", justifyContent: "center", p: 2 }}>
                                    <CircularProgress />
                                </Box>
                            ) : monsters.length === 0 ? (
                                <Typography color="text.secondary">
                                    No monsters found
                                </Typography>
                            ) : (
                                <List>
                                    {monsters
                                        .filter((monster) =>
                                            monster.name
                                                .toLowerCase()
                                                .includes(monsterSearch.toLowerCase())
                                        )
                                        .map((monster: MonsterCombatant) => (
                                            <ListItemButton
                                                key={monster.monster_id}
                                                onClick={() =>
                                                    handleSelectCreature({
                                                        ...monster,
                                                        type: "monster",
                                                    })
                                                }
                                            >
                                                <ListItemText
                                                    primary={monster.name}
                                                    secondary={`CR: ${monster.challenge_rating ?? "-"}`}
                                                />
                                </ListItemButton>
                            ))}
                                </List>
                            )}
                        </Box>
                    )}

                    {/* Создать монстра */}
                    {dialogTab === 1 && (
                        <Box sx={{ pt: 2 }}>
                            <MonsterForm
                                onSubmit={handleCreateMonster}
                                onCancel={() => setOpenDialog(false)}
                            />
                        </Box>
                    )}

                    {/* Добавить игрока */}
                    {dialogTab === 2 && (
                        <Box sx={{ pt: 2 }}>
                            {loadingMonsters ? (
                                <Box
                                    sx={{
                                        display: "flex",
                                        justifyContent: "center",
                                        p: 2,
                                    }}
                                >
                                    <CircularProgress />
                                </Box>
                            ) : characters.length === 0 ? (
                                <Typography color="text.secondary">
                                    No characters found
                                </Typography>
                            ) : (
                                <List>
                                    {characters.map((character: CharacterCombatant) => (
                                        <ListItem
                                            key={character.character_id}
                                            disablePadding
                                        >
                                            <ListItemButton
                                                onClick={() =>
                                                    handleSelectCreature({
                                                        ...character,
                                                        type: "character",
                                                    })
                                                }
                                            >
                                                <ListItemText
                                                    primary={character.name}
                                                    secondary={`Class: ${
                                                        character.character_class ?? "-"
                                                    }`}
                                                />
                                            </ListItemButton>

                                            <IconButton
                                                onClick={() =>
                                                    handleUpdateCharacter()
                                                }
                                                aria-label="edit character"
                                            >
                                                <EditIcon />
                                            </IconButton>

                                            <IconButton
                                                color="error"
                                                onClick={() =>
                                                    handleDeleteCharacter(
                                                        character.character_id
                                                    )
                                                }
                                                aria-label="delete character"
                                            >
                                                <DeleteIcon />
                                            </IconButton>
                                        </ListItem>
                                    ))}
                                </List>
                            )}
                        </Box>
                    )}

                    {/* Создать игрока */}
                    {dialogTab === 3 && (
                        <Box sx={{ pt: 2 }}>
                            <CharacterForm
                                onSubmit={handleCreateCharacter}
                                onCancel={() => setOpenDialog(false)}
                            />
                        </Box>
                    )}
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setOpenDialog(false)}>Cancel</Button>
                </DialogActions>
            </Dialog>
        </>
    );
}