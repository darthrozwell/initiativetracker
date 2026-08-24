import { useState } from "react";
import {
    Box,
    Button,
    Grid,
    MenuItem,
    TextField,
} from "@mui/material";

export interface CharacterAttack {
    title: string;
    name: string;
    text: string;
    attack_type: string;
    attack_range: string;
    hit_bonus: number;
    reach: string;
    damage: string;
}

interface AttackFormProps {
    onSubmit: (attack: CharacterAttack) => void;
    onCancel?: () => void;
}

const initialAttack: CharacterAttack = {
    title: "",
    name: "",
    text: "",
    attack_type: "",
    attack_range: "",
    hit_bonus: 0,
    reach: "",
    damage: "",
};

export default function AttackForm({
    onSubmit,
    onCancel,
}: AttackFormProps) {
    const [form, setForm] = useState<CharacterAttack>(initialAttack);

    const handleChange = <K extends keyof CharacterAttack>(
        field: K,
        value: CharacterAttack[K],
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
                        fullWidth
                        size="small"
                        label="Title"
                        value={form.title}
                        onChange={(e) =>
                            handleChange("title", e.target.value)
                        }
                    />
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
                        label="Attack Type"
                        value={form.attack_type}
                        onChange={(e) =>
                            handleChange("attack_type", e.target.value)
                        }
                    >
                        <MenuItem value="Melee">Melee</MenuItem>
                        <MenuItem value="Ranged">Ranged</MenuItem>
                        <MenuItem value="Melee or Ranged">
                            Melee or Ranged
                        </MenuItem>
                    </TextField>
                </Grid>

                <Grid size={{ xs: 12, sm: 6 }}>
                    <TextField
                        fullWidth
                        size="small"
                        label="Attack Range"
                        placeholder="e.g. 5 ft."
                        value={form.attack_range}
                        onChange={(e) =>
                            handleChange("attack_range", e.target.value)
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
