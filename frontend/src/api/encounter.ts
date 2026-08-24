const API = "http://127.0.0.1:8000"

export async function createEncounter(payload:{
                                                    name: string,
                                                    round: number,
                                                    current_turn: number
                                                }
)
{
    const response = await fetch(`${API}/encounter/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            encounter: payload
        }),
    });

    if (!response.ok) {
        throw new Error("Failed to create encounter");
    }

    return response.json();
}

export async function getEncounter(id: string) {
    const response = await fetch(`${API}/encounter/${id}`);

    if (!response.ok) {
        throw new Error("Encounter not found");
    }

    return response.json();
}

export async function getAllEncounters() {
    const response = await fetch(`${API}/encounter/`);

    if (!response.ok) {
        throw new Error("Encounters not found");
    }

    return response.json();
}

export async function deleteEncounter(id: string) {
    const response = await fetch(`${API}/encounter/${id}`, {
        method: "DELETE",
    });

    if (!response.ok) {
        throw new Error("Failed to delete encounter");
    }

    return
}

export async function updateEncounter(id: string, payload:{
                                                    name?: string,
                                                    round?: number,
                                                    current_turn?: number
                                                    }
                                                    )
{
    // Backend expects body { "encounter": { ... } } because of Body(embed=True)
    const response = await fetch(`${API}/encounter/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ encounter: payload }),
    });

    if (!response.ok) {
        throw new Error("Failed to update encounter");
    }

    return response.json();
}


export async function getAllCombatants(
    encounterId: string
){
    const response = await fetch(`${API}/encounter/${encounterId}/combatant`);
    if (!response.ok) {
        throw new Error("Combatants not found");
    }
    return response.json();
}

export async function createCombatant(
    encounterId: string,
    payload: {
        monster_id?: string
        character_id?: string
        nickname: string
        current_hp: number
        current_initiative: number
        status: string
    }
){
     const response = await fetch(
        `${API}/encounter/${encounterId}/combatant`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({combatant: payload}),
        },
    )
    if (!response.ok) {
    const error = await response.json();
    console.error("Backend validation error:", error);
    throw new Error(JSON.stringify(error));
}
    return response.json();
}


export async function updateCombatant(
    encounterId: string,
    combatantId: string,
    payload: {
        monster_id?: string
        current_hp?: number
        current_initiative?: number
        nickname?: string
        status?: string
    },
) {
    const response = await fetch(
        `${API}/encounter/${encounterId}/combatant/${combatantId}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({combatant: payload}),
        },
    );
    if (!response.ok) {
        throw new Error("Failed to update combatant");
    }
    return response.json();
}

export async function deleteCombatant(
    encounterId: string,
    combatantId: string,
) {
    const response = await fetch(
        `${API}/encounter/${encounterId}/combatant/${combatantId}`,
        {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        },
    );
    if (!response.ok) {
        throw new Error("Failed to delete combatant");
    }
    return
}
