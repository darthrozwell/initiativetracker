import {useState} from "react";
import {
    Box,
    Button, Checkbox, Dialog, DialogContent, DialogTitle,
    Divider, FormControlLabel,
    Grid,
    MenuItem,
    TextField,
    Typography,
} from "@mui/material";
import type {DamageType, MonsterAlignment, MonsterCreationForm, MonsterSize, MonsterType} from "../types/combat.ts"
import AttackForm from "./AddAttackForm.tsx";

const monster_sizes: MonsterSize[] = [
    "Крошечный",
    "Маленький",
    "Средний",
    "Большой",
    "Огромный",
    "Громадный",
]

const monster_types: MonsterType[] = [
    "Аберрация",
    "Зверь",
    "Небожитель",
    "Конструкт",
    "Дракон",
    "Элементаль",
    "Фея",
    "Исчадие",
    "Великан",
    "Гуманоид",
    "Чудовище",
    "Слизь",
    "Растение",
    "Нежить",
]

const monster_alignments: MonsterAlignment[] = [
    "Нейтральный",
    "Нейтральный Добрый",
    "Нейтральный Злой",
    "Принципиальный Добрый",
    "Принципиальный Злой",
    "Принципиальный Нейтральный",
    "Хаотичный Добрый",
    "Хаотичный Злой",
    "Хаотичный Нейтральный",
]

const damage_types: DamageType[] = [
    "Дробящий",
    "Колющий",
    "Рубящий",
    "Кислота",
    "Холод",
    "Огонь",
    "Силовой",
    "Электричество",
    "Некротический",
    "Яд",
    "Психический",
    "Излучение",
    "Звук",
]

const initialForm: MonsterCreationForm = {
    name: "",
    source:"Custom",
    size: "Средний",
    creature_type: "Гуманоид",
    alignment: "Нейтральный",

    armor_class: 10,
    initiative: 0,
    speed: "30 feet",
    hit_points_value: 10,

    protections: {
        damage_resistance: [],
        damage_immunity: [],
        damage_vulnerability: []
    },

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

    hit_points_formula: "1",
    challenge_rating: "1",
    experience: 0,
    proficiency_bonus: 1,
    skills: "",
    senses: "",
    languages: "",
    equipment: "",
    treasure: "",
    habitat: "",
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


interface MonsterFormProps {
    onSubmit: (data: MonsterCreationForm) => void
    onCancel?: () => void
}

export default function MonsterForm({
    onSubmit,
    onCancel,
}: MonsterFormProps) {
    const [form, setForm] = useState<MonsterCreationForm>(initialForm)
    const [openAttackDialog, setOpenAttackDialog] = useState(false)

    const handleChange = (
        field: keyof MonsterCreationForm,
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
                            label="Type"
                            value={form.creature_type}
                            onChange={(e) =>
                                handleChange(
                                    "creature_type",
                                    e.target.value,
                                )
                            }
                        >
                            {monster_types.map((monster_type) => (
                                <MenuItem key={monster_type} value={monster_type}>
                                    {monster_type}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid size={{ xs:2 }}>
                        <TextField
                            select
                            fullWidth
                            label="Alignment"
                            value={form.alignment}
                            onChange={(e) =>
                                handleChange("alignment", e.target.value)
                            }
                        >
                            {monster_alignments.map((alignment) => (
                                <MenuItem key={alignment} value={alignment}>
                                    {alignment}
                                </MenuItem>
                            ))}
                        </TextField>
                    </Grid>

                    <Grid size={{ xs:2 }}>
                        <TextField
                            select
                            fullWidth
                            label="Size"
                            value={form.size}
                            onChange={(e) =>
                                handleChange("size", e.target.value)
                            }
                        >
                            {monster_sizes.map((size) => (
                                <MenuItem key={size} value={size}>
                                    {size}
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
                            select
                            fullWidth
                            label="Damage Resistance"
                            value={form.protections.damage_resistance ?? []}
                            onChange={(e) => {
                                const value = e.target.value;

                                setForm((prev) => ({
                                    ...prev,
                                    protections: {
                                        ...prev.protections,
                                        damage_resistance: (
                                            Array.isArray(value)
                                                ? value
                                                : value.split(",")
                                        ) as DamageType[],
                                    },
                                }));
                            }}
                            slotProps={{
                                select: {
                                    multiple: true,
                                    renderValue: (selected) =>
                                        (selected as DamageType[]).join(", "),
                                },
                            }}
                        >
                            {damage_types.map((damageType) => (
                                <MenuItem key={damageType} value={damageType}>
                                    {damageType}
                                </MenuItem>
                            ))}
                        </TextField>
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
                            select
                            fullWidth
                            label="Damage Immunity"
                            value={form.protections.damage_immunity ?? []}
                            onChange={(e) => {
                                const value = e.target.value;

                                setForm((prev) => ({
                                    ...prev,
                                    protections: {
                                        ...prev.protections,
                                        damage_immunity: (
                                            Array.isArray(value)
                                                ? value
                                                : value.split(",")
                                        ) as DamageType[],
                                    },
                                }));
                            }}
                            slotProps={{
                                select: {
                                    multiple: true,
                                    renderValue: (selected) =>
                                        (selected as DamageType[]).join(", "),
                                },
                            }}
                        >
                            {damage_types.map((damageType) => (
                                <MenuItem key={damageType} value={damageType}>
                                    {damageType}
                                </MenuItem>
                            ))}
                        </TextField>
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
                            select
                            fullWidth
                            label="Damage Vulnerability"
                            value={form.protections.damage_vulnerability ?? []}
                            onChange={(e) => {
                                const value = e.target.value;

                                setForm((prev) => ({
                                    ...prev,
                                    protections: {
                                        ...prev.protections,
                                        damage_vulnerability: (
                                            Array.isArray(value)
                                                ? value
                                                : value.split(",")
                                        ) as DamageType[],
                                    },
                                }));
                            }}
                            slotProps={{
                                select: {
                                    multiple: true,
                                    renderValue: (selected) =>
                                        (selected as DamageType[]).join(", "),
                                },
                            }}
                        >
                            {damage_types.map((damageType) => (
                                <MenuItem key={damageType} value={damageType}>
                                    {damageType}
                                </MenuItem>
                            ))}
                        </TextField>
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
                                    {attack.name || attack.type}
                                </Typography>

                                <Typography
                                    variant="body2"
                                    color="text.secondary"
                                >
                                    {attack.damage[0].damage_type}
                                    {" · "}
                                    {attack.damage[0].damage}
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
                        Создать монстра
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