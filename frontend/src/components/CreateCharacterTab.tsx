import {useState} from "react";
import {
    Box,
    Button, Checkbox,
    Dialog,
    DialogContent, DialogTitle,
    Divider, FormControlLabel,
    Grid,
    MenuItem,
    TextField,
    Typography,
} from "@mui/material";
import type {CharacterClass, CharacterCreationForm, Race} from "../types/combat.ts"
import AttackForm from "./AddAttackForm.tsx";

const characterClasses: CharacterClass[] = [
    "Artificer",
    "Bard",
    "Barbarian",
    "Fighter",
    "Wizard",
    "Druid",
    "Cleric",
    "Warlock",
    "Monk",
    "Paladin",
    "Rogue",
    "Ranger",
    "Sorcerer",
]

const races: Race[] = [
    "Aasimar",
    "Gnome",
    "Goliath",
    "Dwarf",
    "Dragonborn",
    "Orc",
    "Halfling",
    "Tiefling",
    "Human",
    "Elf",
];

const initialForm: CharacterCreationForm = {
    name: "",
    source:"Custom",
    character_class: "Fighter",
    race: "Human",
    alignment: "Нейтральный",

    armor_class: 10,
    initiative: 0,
    speed: "30 feet",
    hit_points_value: 10,

    damage_resistance: "",
    damage_immunity: "",
    damage_vulnerability: "",

    skills: "",
    senses: "",
    languages: "",
    proficiency_bonus: 1,

    strength_value: 10,
    is_strength_save: false,

    dexterity_value: 10,
    is_dexterity_save: false,

    constitution_value: 10,
    is_constitution_save: false,

    intelligence_value: 10,
    is_intelligence_save: false,

    wisdom_value: 10,
    is_wisdom_save: false,

    charisma_value: 10,
    is_charisma_save: false,

    actions: [],
}

interface AbilityFieldsProps {
    name: string
    value: number
    save: boolean
    onValueChange: (value: number) => void
    onSaveChange: (value: boolean) => void
}

function AbilityFields({
    name,
    value,
    save,
    onValueChange,
    onSaveChange,
}: AbilityFieldsProps) {
    return (
        <Grid size={{ xs: 2 }} sx={{textAlign: 'center'}}>
            <Typography variant="subtitle1" sx={{ mb: 1 }}>
                {name}
            </Typography>

            <Grid container spacing={1} justifyContent={"space-around"}>
                <Grid size={{ xs: 4 }}>
                    <TextField
                        fullWidth
                        size="small"
                        type="number"
                        label="Value"
                        value={value}
                        onChange={(e) =>
                            onValueChange(Number(e.target.value))
                        }
                    />
                </Grid>

                 <Grid
                    size={{ xs: 4 }}
                    sx={{
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                    }}
                >
                    <FormControlLabel
                        control={
                            <Checkbox
                                checked={save}
                                onChange={(e) =>
                                    onSaveChange(e.target.checked)
                                }
                            />
                        }
                        label="Save"
                    />
                </Grid>
            </Grid>
        </Grid>
    )
}


interface CharacterFormProps {
    onSubmit: (data: CharacterCreationForm) => void
    onCancel?: () => void
}

export default function CharacterForm({
    onSubmit,
    onCancel,
}: CharacterFormProps) {
    const [form, setForm] = useState<CharacterCreationForm>(initialForm)
    const [openAttackDialog, setOpenAttackDialog] = useState(false)

    const handleChange = (
        field: keyof CharacterCreationForm,
        value: string | number | boolean | null,
    ) => {
        setForm((prev) => ({
            ...prev,
            [field]: value,
        }))
    }

    return (
        <>
            <Box component="form" onSubmit={(event) => {
                                                    event.preventDefault();
                                                    onSubmit(form)
                                                }}
            >
                {/* Основная информация */}
                <Divider sx={{ my: 3 }} />

                <Grid container spacing={2}>
                    <Grid size={{ xs: 6 }}>
                        <TextField
                            fullWidth
                            required
                            label="Имя"
                            value={form.name}
                            onChange={(e) =>
                                handleChange("name", e.target.value)
                            }
                        />
                    </Grid>

                    <Grid size={{ xs: 2 }}>
                        <TextField
                            fullWidth
                            type="number"
                            label="Armor Class"
                            value={form.armor_class}
                            onChange={(e) =>
                                handleChange(
                                    "armor_class",
                                    Number(e.target.value),
                                )
                            }
                        />
                    </Grid>

                    <Grid size={{ xs: 2 }}>
                        <TextField
                            fullWidth
                            type="number"
                            label="Initiative"
                            value={form.initiative}
                            onChange={(e) =>
                                handleChange(
                                    "initiative",
                                    Number(e.target.value),
                                )
                            }
                        />
                    </Grid>

                    <Grid size={{ xs: 2 }}>
                        <TextField
                            fullWidth
                            type="number"
                            label="Hit Points"
                            value={form.hit_points_value}
                            onChange={(e) =>
                                handleChange(
                                    "hit_points_value",
                                    Number(e.target.value),
                                )
                            }
                        />
                    </Grid>

                    <Grid size={{ xs: 2 }}>
                        <TextField
                            select
                            fullWidth
                            label="Класс"
                            value={form.character_class}
                            onChange={(e) =>
                                handleChange(
                                    "character_class",
                                    e.target.value,
                                )
                            }
                        >
                            {characterClasses.map((characterClass) => (
                                <MenuItem key={characterClass} value={characterClass}>
                                    {characterClass}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid size={{ xs:2 }}>
                        <TextField
                            select
                            fullWidth
                            label="Раса"
                            value={form.race}
                            onChange={(e) =>
                                handleChange("race", e.target.value)
                            }
                        >
                            {races.map((race) => (
                                <MenuItem key={race} value={race}>
                                    {race}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid size={{ xs: 2 }}>
                        <TextField
                            fullWidth
                            type="number"
                            label="Proficiency bonus"
                            value={form.proficiency_bonus}
                            onChange={(e) =>
                                handleChange(
                                    "proficiency_bonus",
                                    Number(e.target.value),
                                )
                            }
                        />
                    </Grid>

                    <Grid size={{ xs: 6 }}>
                        <TextField
                            fullWidth
                            label="Speed"
                            value={form.speed}
                            onChange={(e) =>
                                handleChange("speed", e.target.value)
                            }
                        />
                    </Grid>
                </Grid>

                <Divider sx={{ my: 3 }} />

                {/* Сопротивления */}
                <Grid container spacing={2} justifyContent={"center"} alignItems={"flex-end"} >
                    <Grid size={{ xs: 8 }}>
                        <TextField
                            fullWidth
                            label="Damage Resistance"
                            value={form.damage_resistance ?? ""}
                            onChange={(e) =>
                                handleChange(
                                    "damage_resistance",
                                    e.target.value || null,
                                )
                            }
                        />
                    </Grid>

                    <AbilityFields
                        name="Strength"
                        value={form.strength_value}
                        save={form.is_strength_save}
                        onValueChange={(value) =>
                            handleChange("strength_value", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("is_strength_save", value)
                        }
                    />

                    <AbilityFields
                        name="Dexterity"
                        value={form.dexterity_value}
                        save={form.is_dexterity_save}
                        onValueChange={(value) =>
                            handleChange("dexterity_value", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("is_dexterity_save", value)
                        }
                    />

                    <Grid size={{ xs: 8 }}>
                        <TextField
                            fullWidth
                            label="Damage Immunity"
                            value={form.damage_immunity ?? ""}
                            onChange={(e) =>
                                handleChange(
                                    "damage_immunity",
                                    e.target.value || null,
                                )
                            }
                        />
                    </Grid>

                    <AbilityFields
                        name="Constitution"
                        value={form.constitution_value}
                        save={form.is_constitution_save}
                        onValueChange={(value) =>
                            handleChange("constitution_value", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("is_constitution_save", value)
                        }
                    />

                    <AbilityFields
                        name="Intelligence"
                        value={form.intelligence_value}
                        save={form.is_intelligence_save}
                        onValueChange={(value) =>
                            handleChange("intelligence_value", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("is_intelligence_save", value)
                        }
                    />

                    <Grid size={{ xs: 8 }}>
                        <TextField
                            fullWidth
                            label="Damage Vulnerability"
                            value={form.damage_vulnerability ?? ""}
                            onChange={(e) =>
                                handleChange(
                                    "damage_vulnerability",
                                    e.target.value || null,
                                )
                            }
                        />
                    </Grid>

                    <AbilityFields
                        name="Wisdom"
                        value={form.wisdom_value}
                        save={form.is_wisdom_save}
                        onValueChange={(value) =>
                            handleChange("wisdom_value", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("is_wisdom_save", value)
                        }
                    />

                    <AbilityFields
                        name="Charisma"
                        value={form.charisma_value}
                        save={form.is_charisma_save}
                        onValueChange={(value) =>
                            handleChange("charisma_value", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("is_charisma_save", value)
                        }
                    />

                </Grid>

                <Button
                    variant="outlined"
                    onClick={() => setOpenAttackDialog(true)}
                    sx={{ mt: 4 }}
                >
                    Add Attack
                </Button>



                <Box sx={{ mt: 2 }}>
                    <Typography variant="h6">
                        Attacks
                    </Typography>

                    {form.actions?.map((attack, index) => (
                        <Box
                            key={index}
                            sx={{
                                display: "flex",
                                alignItems: "center",
                                justifyContent: "space-between",
                                py: 1,
                            }}
                        >
                            <Box>
                                <Typography>
                                    {attack.name || attack.title}
                                </Typography>

                                <Typography
                                    variant="body2"
                                    color="text.secondary"
                                >
                                    {attack.attack_type}
                                    {" · "}
                                    {attack.damage}
                                    {" · "}
                                    +{attack.hit_bonus}
                                </Typography>
                            </Box>

                            <Button
                                size="small"
                                color="error"
                                onClick={() => {
                                    setForm((prev) => ({
                                        ...prev,
                                        actions: prev.actions?.filter(
                                            (_, i) => i !== index
                                        ),
                                    }));
                                }}
                            >
                                Delete
                            </Button>
                        </Box>
                    ))}
                </Box>


                <Box
                    sx={{
                        display: "flex",
                        justifyContent: "flex-end",
                        gap: 2,
                        mt: 3,
                    }}
                >
                    {onCancel && (
                        <Button onClick={onCancel}>
                            Отмена
                        </Button>
                    )}

                    <Button
                        type="submit"
                        variant="contained"
                    >
                        Создать персонажа
                    </Button>
                </Box>


            </Box>

            <Dialog
                open={openAttackDialog}
                onClose={() => setOpenAttackDialog(false)}
                maxWidth="md"
                fullWidth
                disableRestoreFocus
            >
                <DialogTitle>
                    Add Attack
                </DialogTitle>

                <DialogContent>
                    <AttackForm
                        onSubmit={(attack) => {
                            setForm((prev) => ({
                                ...prev,
                                actions: [
                                    ...(prev.actions ?? []),
                                    attack,
                                ],
                            }));

                            setOpenAttackDialog(false);
                        }}
                        onCancel={() => setOpenAttackDialog(false)}
                    />
                </DialogContent>
            </Dialog>
        </>

    )
}