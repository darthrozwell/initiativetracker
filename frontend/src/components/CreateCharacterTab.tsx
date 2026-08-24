import {useState} from "react";
import {
    Box,
    Button,
    Dialog,
    DialogContent, DialogTitle,
    Divider,
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

    armor_class: 10,
    initiative: 0,
    speed: "30 feet",
    hit_points_value: 10,

    damage_resistance: "",
    damage_immunity: "",
    damage_vulnerability: "",

    strength_value: 10,
    strength_mod: 0,
    strength_save: 0,

    dexterity_value: 10,
    dexterity_mod: 0,
    dexterity_save: 0,

    constitution_value: 10,
    constitution_mod: 0,
    constitution_save: 0,

    intelligence_value: 10,
    intelligence_mod: 0,
    intelligence_save: 0,

    wisdom_value: 10,
    wisdom_mod: 0,
    wisdom_save: 0,

    charisma_value: 10,
    charisma_mod: 0,
    charisma_save: 0,

    abilities: [],
};

interface AbilityFieldsProps {
    name: string
    value: number
    modifier: number
    save: number
    onValueChange: (value: number) => void
    onModifierChange: (value: number) => void
    onSaveChange: (value: number) => void
}

function AbilityFields({
    name,
    value,
    modifier,
    save,
    onValueChange,
    onModifierChange,
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

                <Grid size={{ xs: 4 }}>
                    <TextField
                        fullWidth
                        size="small"
                        type="number"
                        label="Mod"
                        value={modifier}
                        onChange={(e) =>
                            onModifierChange(Number(e.target.value))
                        }
                    />
                </Grid>

                <Grid size={{ xs: 4 }}>
                    <TextField
                        fullWidth
                        size="small"
                        type="number"
                        label="Save"
                        value={save}
                        onChange={(e) =>
                            onSaveChange(Number(e.target.value))
                        }
                    />
                </Grid>
            </Grid>
        </Grid>
    );
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
        value: string | number | null,
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

                    <Grid size={{ xs: 3 }}>
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

                    <Grid size={{ xs:3 }}>
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
                        modifier={form.strength_mod}
                        save={form.strength_save}
                        onValueChange={(value) =>
                            handleChange("strength_value", value)
                        }
                        onModifierChange={(value) =>
                            handleChange("strength_mod", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("strength_save", value)
                        }
                    />

                    <AbilityFields
                        name="Dexterity"
                        value={form.dexterity_value}
                        modifier={form.dexterity_mod}
                        save={form.dexterity_save}
                        onValueChange={(value) =>
                            handleChange("dexterity_value", value)
                        }
                        onModifierChange={(value) =>
                            handleChange("dexterity_mod", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("dexterity_save", value)
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
                        modifier={form.constitution_mod}
                        save={form.constitution_save}
                        onValueChange={(value) =>
                            handleChange("constitution_value", value)
                        }
                        onModifierChange={(value) =>
                            handleChange("constitution_mod", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("constitution_save", value)
                        }
                    />

                    <AbilityFields
                        name="Intelligence"
                        value={form.intelligence_value}
                        modifier={form.intelligence_mod}
                        save={form.intelligence_save}
                        onValueChange={(value) =>
                            handleChange("intelligence_value", value)
                        }
                        onModifierChange={(value) =>
                            handleChange("intelligence_mod", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("intelligence_save", value)
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
                        modifier={form.wisdom_mod}
                        save={form.wisdom_save}
                        onValueChange={(value) =>
                            handleChange("wisdom_value", value)
                        }
                        onModifierChange={(value) =>
                            handleChange("wisdom_mod", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("wisdom_save", value)
                        }
                    />

                    <AbilityFields
                        name="Charisma"
                        value={form.charisma_value}
                        modifier={form.charisma_mod}
                        save={form.charisma_save}
                        onValueChange={(value) =>
                            handleChange("charisma_value", value)
                        }
                        onModifierChange={(value) =>
                            handleChange("charisma_mod", value)
                        }
                        onSaveChange={(value) =>
                            handleChange("charisma_save", value)
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

                    {form.abilities?.map((attack, index) => (
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
                                        abilities: prev.abilities?.filter(
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
                                abilities: [
                                    ...(prev.abilities ?? []),
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