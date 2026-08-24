// src/components/StatCard.tsx

import { useState } from "react";

import {
    Paper,
    TextField,
    Typography,
} from "@mui/material"

interface StatCardProps {
    title: string
    value: string | number
    editable?: boolean
    onChange?: (value: number) => void | Promise<void>
}

export default function StatCard({
    title,
    value,
    editable = false,
    onChange,
}: StatCardProps) {
    const [editing, setEditing] = useState(false)
    const [inputValue, setInputValue] = useState(String(value))

    const startEditing = () => {
        if (!editable) return

        setInputValue(String(value))
        setEditing(true)
    }

    const saveValue = async () => {
        const newValue = Number(inputValue)

        if (Number.isNaN(newValue)) {
            setInputValue(String(value))
            setEditing(false)
            return;
        }

        if (newValue !== Number(value)) {
            await onChange?.(newValue)
        }

        setEditing(false)
    }

    const handleKeyDown = (
        event: React.KeyboardEvent<HTMLInputElement>,
    ) => {
        if (event.key === "Enter") {
            event.currentTarget.blur()
        }

        if (event.key === "Escape") {
            setInputValue(String(value))
            setEditing(false)
        }
    };

    return (
        <Paper
            sx={{
                p: 0.5,
                height: "100%",
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                textAlign: "center",
            }}
        >
            <Typography
                variant="caption"
                color="text.secondary"
                sx={{
                    p: 0.5,
                    textTransform: "uppercase",
                    letterSpacing: 1,
                }}
            >
                {title}
            </Typography>

            {editing ? (
                <TextField
                    autoFocus
                    variant="standard"
                    type="number"
                    value={inputValue}
                    onChange={(event) =>
                        setInputValue(event.target.value)
                    }
                    onBlur={saveValue}
                    onKeyDown={handleKeyDown}
                    sx={{
                        pb: 1,
                        width: "60px",
                        alignSelf: "center",
                        "& input": {
                            textAlign: "center",
                            fontSize: "1.25rem",
                            fontWeight: 580,
                        },
                    }}
                />
            ) : (
                <Typography
                    variant="h6"
                    onClick={startEditing}
                    sx={{
                        pb: 1,
                        fontWeight: 580,
                        lineHeight: 1.2,
                        cursor: editable ? "pointer" : "default",
                    }}
                >
                    {value}
                </Typography>
            )}
        </Paper>
    )
}