import { useState, useEffect } from "react";
import {
    Box,
    Button,
    Typography,
    CircularProgress,
    List,
    ListItem,
    ListItemButton,
    ListItemText,
    IconButton,
    Divider,
    TextField,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import SaveIcon from "@mui/icons-material/Save";
import CancelIcon from "@mui/icons-material/Cancel";
import { useNavigate } from "react-router-dom";
import { createEncounter, getAllEncounters, deleteEncounter, updateEncounter } from "../api/encounter";
import type {Encounter} from "../types/combat.ts";

export default function EncounterList() {
    const [creating, setCreating] = useState(false);
    const [loading, setLoading] = useState(true);
    const [encounters, setEncounters] = useState<Encounter[]>([]);
    const [pendingDeletes, setPendingDeletes] = useState<Record<string, { timer: number; item: any }>>({});
    const [editingId, setEditingId] = useState<string | null>(null);
    const [editingName, setEditingName] = useState("");
    const [savingId, setSavingId] = useState<string | null>(null);

    const navigate = useNavigate();

    async function loadList() {
        setLoading(true);
        try {
            const data = await getAllEncounters();
            setEncounters(data ?? []);
        } catch (err) {
            console.error("Failed to load encounters", err);
            setEncounters([]);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        let mounted = true;
        (async () => {
            if (!mounted) return;
            await loadList();
        })();
        return () => {
            mounted = false;
        };
    }, []);

    async function handleCreate() {
        setCreating(true);
        try {
            const payload = {name: "New encounter", round: 0, current_turn: 0}
            const created = await createEncounter(payload);
            const id = created?.encounter_id;
            if (id) {
                navigate(`/encounter/${id}`);
                return;
            }
            await loadList();
        } catch (err) {
            console.error(err);
            alert("Failed to create encounter");
        } finally {
            setCreating(false);
        }
    }

    async function handleDelete(id: string) {
        const ok = window.confirm("Delete this encounter? You can undo for 5 seconds.");
        if (!ok) return;

        // Find item
        const item = encounters.find(e => e.encounter_id === id);
        // Start delayed deletion
        const timer = window.setTimeout(async () => {
            try {
                await deleteEncounter(id);
                setEncounters(prev => prev.filter(e => e.encounter_id !== id));
            } catch (err) {
                console.error(err);
                alert("Failed to delete encounter on server");
            } finally {
                setPendingDeletes(prev => {
                    const copy = { ...prev };
                    delete copy[id];
                    return copy;
                });
            }
        }, 5000);

        setPendingDeletes(prev => ({ ...prev, [id]: { timer, item } }));
    }

    function undoDelete(id: string) {
        const entry = pendingDeletes[id];
        if (!entry) return;
        window.clearTimeout(entry.timer);
        setPendingDeletes(prev => {
            const copy = { ...prev };
            delete copy[id];
            return copy;
        });
    }

    function startEditing(e: any) {
        setEditingId(e.encounter_id);
        setEditingName(e.name ?? "");
    }

    async function saveEdit(id: string) {
        if (!editingName.trim()) {
            alert("Name cannot be empty");
            return;
        }

        setSavingId(id);
        try {
            const item = encounters.find(e => e.encounter_id === id);
            const payload = { ...item, name: editingName };
            await updateEncounter(id, {name: editingName});
            setEncounters(prev => prev.map(e => e.encounter_id === id ? payload : e));
            setEditingId(null);
        } catch (err) {
            console.error(err);
            alert("Failed to update encounter");
        } finally {
            setSavingId(null);
        }
    }

    function cancelEdit() {
        setEditingId(null);
        setEditingName("");
    }

    return (
        <Box sx={{ p: 4 }}>
            <Box sx={{ display: "flex", alignItems: "center", justifyContent: "space-between", mb: 2 }}>
                <Box>
                    <Typography variant="h4">Encounters</Typography>
                    <Typography color="text.secondary">Manage saved encounters</Typography>
                </Box>

                <Button variant="contained" onClick={handleCreate} disabled={creating}>
                    {creating ? <CircularProgress size={20} /> : "Create new encounter"}
                </Button>
            </Box>

            <Divider sx={{ mb: 2 }} />

            {loading ? (
                <CircularProgress />
            ) : encounters.length === 0 ? (
                <Typography color="text.secondary">No encounters found. Create one to begin.</Typography>
            ) : (
                <List>
                    {encounters.map((e: Encounter) => {
                        const pending = pendingDeletes[e.encounter_id];
                        return (
                            <ListItem
                                key={e.encounter_id}
                                secondaryAction={
                                    pending ? (
                                        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                            <Typography variant="caption" color="text.secondary">Deleting…</Typography>
                                            <Button size="small" onClick={() => undoDelete(e.encounter_id)}>Undo</Button>
                                        </Box>
                                     ) : (
                                        <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
                                            {editingId === e.encounter_id ? (
                                                <>
                                                    <IconButton edge="end" color="success" onClick={() => saveEdit(e.encounter_id)} disabled={savingId === e.encounter_id}>
                                                        {savingId === e.encounter_id ? <CircularProgress size={18} /> : <SaveIcon />}
                                                    </IconButton>
                                                    <IconButton edge="end" color="inherit" onClick={cancelEdit}>
                                                        <CancelIcon />
                                                    </IconButton>
                                                </>
                                            ) : (
                                                <>
                                                    <IconButton edge="end" color="primary" onClick={() => startEditing(e)}>
                                                        <EditIcon />
                                                    </IconButton>

                                                    <IconButton edge="end" color="error" onClick={() => handleDelete(e.encounter_id)}>
                                                        <DeleteIcon />
                                                    </IconButton>
                                                </>
                                            )}
                                        </Box>
                                    )
                                        }
                                    >
                                        {editingId === e.encounter_id ? (
                                            <Box sx={{ p: 1, flex: 1 }}>
                                                <TextField
                                                    autoFocus
                                                    size="small"
                                                    fullWidth
                                                    value={editingName}
                                                    onChange={(ev) => setEditingName(ev.target.value)}
                                                    onKeyDown={(ev) => {
                                                        if (ev.key === "Enter") saveEdit(e.encounter_id);
                                                        if (ev.key === "Escape") cancelEdit();
                                                    }}
                                                    placeholder="Encounter name"
                                                />
                                            </Box>
                                        ) : (
                                            <ListItemButton onClick={() => !pending && navigate(`/encounter/${e.encounter_id}`)} disabled={!!pending}>
                                                <ListItemText primary={e.name ?? "Unnamed"} secondary={`Round ${e.round ?? 0}`} />
                                            </ListItemButton>
                                        )}
                                    </ListItem>
                        );
                    })}
                </List>
            )}
        </Box>
    );
}
