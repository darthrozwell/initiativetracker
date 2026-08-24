import type {CharacterCreationForm} from "../types/combat.ts";

const API = "http://127.0.0.1:8000"

export async function createCharacter(
    payload: CharacterCreationForm
){
     const response = await fetch(
        `${API}/character/`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({character: payload}),
        },
    );
    if (!response.ok) {
    const error = await response.json();
    console.error("Backend validation error:", error);
    throw new Error(JSON.stringify(error));
}
    return response.json();
}


export async function getAllCharacters()   {
    const response = await fetch(`${API}/character/`)

    if (!response.ok) {
        throw new Error("Failed to fetch characters")
    }

    return response.json();
}


export async function deleteCharacter(
    character_id: string
)   {
    const response = await fetch(
        `${API}/character/${character_id}`,
        {
            method: "DELETE",
        }
    )

    if (!response.ok) {
        throw new Error("Failed to delete character")
    }
}
