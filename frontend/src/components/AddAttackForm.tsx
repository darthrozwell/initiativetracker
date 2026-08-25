import { useState } from "react";
import {
    Box,
    Button,
    Grid,
    MenuItem,
    TextField,
} from "@mui/material";

import type {Action, ActionType, DamageType} from "../types/combat.ts"


interface AttackFormProps {
    onSubmit: (attack: Action) => void;
    onCancel?: () => void;
}

const initialAttack: Action = {
    type: "Особенности",
    name: "",
    text: "",
    range: "",
    reach: "",
    hit_bonus: 0,
    damage: "",
    damage_type: "Дробящий урон",
}

const damage_types: DamageType[] = [
    "Дробящий урон",
    "Колющий урон",
    "Рубящий урон",
    "урон Кислотой",
    "урон Холодом",
    "урон Огнём",
    "Силовой урон",
    "урон Электричеством",
    "Некротический урон",
    "урон Ядом",
    "Психический урон",
    "урон Излучением",
    "урон Звуком",
]

const action_types: ActionType[] = [
    "Действия",
    "Бонусные действия",
    "Реакции",
    "Легендарные действия",
    "Особенности",
]

export default function AttackForm({
    onSubmit,
    onCancel,
}: AttackFormProps) {
    const [form, setForm] = useState<Action>(initialAttack);

    const handleChange = <K extends keyof Action>(
        field: K,
        value: string | number | DamageType | ActionType
    ) => {
        setForm((prev) => ({
            ...prev,
            [field]: value,
        }));
    };

    const handleSubmit = (event: React.SubmitEvent<HTMLFormElement>) => {
        event.preventDefault()
        onSubmit(form)
    }

    return (
        <Box
            component="form"
            onSubmit={handleSubmit}
            sx={{ mt: 2 }}
        >
            <Grid container spacing={2}>

                <Grid size={{ xs: 12, sm: 6 }}>
                    <TextField
                        select
                        fullWidth
                        size="small"
                        label="Title"
                        value={form.type}
                        onChange={(e) =>
                            handleChange("type", e.target.value)
                        }
                    >
                    {action_types.map((act) => (
                                <MenuItem key={act} value={act}>
                                    {act}
                                </MenuItem>
                            ))}
                    </TextField>
                </Grid>

                <Grid size={{ xs: 12, sm: 6 }}>
                    <TextField
                        fullWidth
                        size="small"
                        label="Name"
                        value={form.name}
                        onChange={(e) =>
                            handleChange("name", e.target.value)
                        }
                    />
                </Grid>

                <Grid size={{ xs: 12, sm: 6 }}>
                    <TextField
                        select
                        fullWidth
                        size="small"
                        label="Damage Type"
                        value={form.damage_type}
                        onChange={(e) =>
                            handleChange("damage_type", e.target.value)
                        }
                    >
                        {damage_types.map((dmg_type) => (
                                <MenuItem key={dmg_type} value={dmg_type}>
                                    {dmg_type}
                                </MenuItem>
                            ))}
                    </TextField>
                </Grid>

                <Grid size={{ xs: 12, sm: 6 }}>
                    <TextField
                        fullWidth
                        size="small"
                        label="Range"
                        placeholder="e.g. 5 ft."
                        value={form.range}
                        onChange={(e) =>
                            handleChange("range", e.target.value)
                        }
                    />
                </Grid>

                <Grid size={{ xs: 12, sm: 4 }}>
                    <TextField
                        fullWidth
                        size="small"
                        type="number"
                        label="Hit Bonus"
                        value={form.hit_bonus}
                        onChange={(e) =>
                            handleChange(
                                "hit_bonus",
                                Number(e.target.value),
                            )
                        }
                    />
                </Grid>

                <Grid size={{ xs: 12, sm: 4 }}>
                    <TextField
                        fullWidth
                        size="small"
                        label="Reach"
                        placeholder="e.g. 5 ft."
                        value={form.reach}
                        onChange={(e) =>
                            handleChange("reach", e.target.value)
                        }
                    />
                </Grid>

                <Grid size={{ xs: 12, sm: 4 }}>
                    <TextField
                        fullWidth
                        size="small"
                        label="Damage"
                        placeholder="e.g. 1d8 + 3 slashing"
                        value={form.damage}
                        onChange={(e) =>
                            handleChange("damage", e.target.value)
                        }
                    />
                </Grid>

                <Grid size={{ xs: 12 }}>
                    <TextField
                        fullWidth
                        multiline
                        minRows={2}
                        label="Description"
                        value={form.text}
                        onChange={(e) =>
                            handleChange("text", e.target.value)
                        }
                    />
                </Grid>

                <Grid
                    size={{ xs: 12 }}
                    sx={{
                        display: "flex",
                        justifyContent: "flex-end",
                        gap: 1,
                    }}
                >
                    {onCancel && (
                        <Button
                            variant="outlined"
                            onClick={onCancel}
                        >
                            Cancel
                        </Button>
                    )}

                    <Button
                        type="submit"
                        variant="contained"
                    >
                        Add Attack
                    </Button>
                </Grid>

            </Grid>
        </Box>
    );
}
