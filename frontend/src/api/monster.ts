import type {MonsterCreationForm} from "../types/combat.ts";

const API = "http://127.0.0.1:8000"

export async function getAllMonsters() {
    const response = await fetch(`${API}/monster/`)

    if (!response.ok) {
        throw new Error("Failed to fetch monsters")
    }

    return response.json();
}

export async function getMonster(name: string) {
    const response = await fetch(`${API}/monster/${name}`)

    if (!response.ok) {
        throw new Error("Monster not found");
    }

    return response.json()
}

export async function createMonster(
    payload: MonsterCreationForm
){
     const response = await fetch(
        `${API}/monster/`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({monster: payload}),
        },
    );
    if (!response.ok) {
    const error = await response.json();
    console.error("Backend validation error:", error);
    throw new Error(JSON.stringify(error));
}
    return response.json();
}
