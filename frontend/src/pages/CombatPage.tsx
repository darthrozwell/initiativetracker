// src/pages/CombatPage.tsx

import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { Box } from "@mui/material"
import Header from "../components/Header"
import Sidebar from "../components/Sidebar"
import CombatPanel from "../components/CombatPanel"
import Footer from "../components/Footer"
import {
    getEncounter,
    updateEncounter,
    updateCombatant,
    createCombatant,
    getAllCombatants,
    deleteCombatant
} from "../api/encounter"
import type {Encounter, Combatant, CombatantPayload, CombatantStatus} from "../types/combat"
import RollSnackbar from "../components/RollSnackbar.tsx"

export default function CombatPage() {

    const [encounter, setEncounter] = useState<Encounter | null>(null)
    const [selected_id, setSelectedId] = useState<number | null>(null)
    const [is_combat_started, setIsCombatStarted] = useState<boolean>(false)
    const [rollResult, setRollResult] = useState<{
        actor: string
        formula: string
        result: number
        bonus: number
    } | null>(null)
    const params = useParams()
    const encounter_id = params.id ?? null

    useEffect(() => {
        if (!encounter_id) return
        async function load() {
            try {
                const data: Encounter = await getEncounter(encounter_id)
                const enc_combatants: Combatant[] = await getAllCombatants(encounter_id) ?? []
                enc_combatants.sort((a, b) => {
                    return(
                        b.current_initiative - a.current_initiative || b.initiative - a.initiative || a.combatant_id.localeCompare(b.combatant_id)
                    )
                })
                setEncounter({...data, combatants: enc_combatants})
                setIsCombatStarted(data.round !== 0)
                if (enc_combatants.length > 0) {
                    setSelectedId(data.current_turn ?? 0)
                }
            } catch (err) {
                console.error("Failed to load encounter", err)
            }
        }
        load();
    }, [encounter_id]);

    async function handleAddCombatant(creature: Combatant) {
        try {
            // creating new combatant
            const payload_combatant: CombatantPayload = {
                monster_id: creature.type === "monster" ? creature.monster_id : null,
                character_id: creature.type === "character" ? creature.character_id : null,
                nickname: creature.name,
                current_hp: creature.hit_points_value,
                current_initiative:
                    Math.floor(Math.random() * 20) + 1 + creature.initiative,
                status: "alive",
            }
            const new_combatant: Combatant = {
                ...creature,
                ...payload_combatant,
                }
            const response = await createCombatant(encounter.encounter_id, payload_combatant)
            new_combatant.combatant_id = response.combatant_id

            // sort by current_initiative then by initiative bonus then by uuid
            const updated_combatants: Combatant[] = [...encounter.combatants ?? [], new_combatant]
            updated_combatants.sort((a, b) => {
                return(
                    b.current_initiative - a.current_initiative || b.initiative - a.initiative || a.combatant_id.localeCompare(b.combatant_id)
                )
            })

            // resolving new current turn (same combatant as prev, but mb new index) and new selected id (new combatant index) or 0, 0 if its first one
            let new_current_turn: number = 0
            let new_selected_id: number = 0
            if (encounter.combatants.length > 1) {
                new_current_turn = updated_combatants.findIndex((comb: Combatant) => comb.combatant_id === encounter.combatants[encounter.current_turn].combatant_id)
                new_selected_id = updated_combatants.findIndex((comb: Combatant) => comb.combatant_id === new_combatant.combatant_id)
            }

            //updating states and back
            await updateEncounter(encounter_id, { current_turn: new_current_turn })
            setEncounter({ ...encounter, combatants: updated_combatants, current_turn: new_current_turn })
            setSelectedId(new_selected_id)

        } catch (err) {
            console.error("Failed to add combatant", err);
            alert("Failed to add combatant");
        }
    }

    async function handleUpdateCombatant(comb_id: string, changes: Partial<Combatant>) {
        if (!encounter || !encounter_id) return
        try {
            await updateCombatant(
                encounter_id,
                comb_id,
                changes,
            )

            setEncounter((prev) => {
                const index = prev.combatants.findIndex(
                    (combatant) =>
                        combatant.combatant_id === comb_id
                );

                if (index === -1) {
                    return prev
                }

                const combatants = [...prev.combatants]

                combatants[index] = {
                    ...combatants[index],
                    ...changes,
                } as Combatant

                combatants.sort((a, b) => {
                    return(
                        b.current_initiative - a.current_initiative || b.initiative - a.initiative || a.combatant_id.localeCompare(b.combatant_id)
                    )
                })

                return {
                    ...prev,
                    combatants,
                }
            })
        } catch (error) {
            console.error(
                "Failed to update combatant:",
                error
            );
        }
    }

    async function handleDeleteCombatant(index: number) {
        if (!encounter || !encounter_id) return
        const ok = window.confirm("Delete this combatant?")
        if (!ok) return

        try {
            // back
            await deleteCombatant(encounter.encounter_id, encounter.combatants[index].combatant_id)
            // store
            const updated_combatants: Combatant[] = (encounter.combatants ?? []).filter((_: Combatant, i: number) => i !== index)
            updated_combatants.sort((a, b) => {
                return(
                    b.current_initiative - a.current_initiative || b.initiative - a.initiative || a.combatant_id.localeCompare(b.combatant_id)
                )
            })

            let new_round: number = encounter.round
            // resolve new current_turn, if deleted then the next one with same index, if it was last then upd round
            let new_current_turn = updated_combatants.findIndex((comb: Combatant) => comb.combatant_id === encounter.combatants[encounter.current_turn].combatant_id)
            if (new_current_turn === -1) {
                new_current_turn = current_turn
                if (new_current_turn >= updated_combatants.length) {
                    new_current_turn = 0
                    new_round += 1
                }
            }
            // resolve new selected_id
            let new_selected_id = updated_combatants.findIndex((comb: Combatant) => comb.combatant_id === encounter.combatants[selected_id].combatant_id)
            if (new_selected_id === -1) {
                new_selected_id = new_current_turn
            }

            // Update local state and back
            await updateEncounter(encounter_id, { current_turn: new_current_turn, round: new_round })
            setEncounter({ ...encounter, combatants: updated_combatants, current_turn: new_current_turn, round: new_round })
            setSelectedId(new_selected_id)
        } catch (err) {
            console.error("Failed to delete combatant", err);
            alert("Failed to delete combatant");
        }
    }


    async function handleNextTurn() {
        if (!encounter || !encounter_id) return
        const combatants: Combatant[] = encounter.combatants ?? []
        if (combatants.length === 0) return

        let new_current_turn: number = (encounter.current_turn ?? 0)
        let new_round: number = encounter.round ?? 0
        // if combatant not alive we skip it
        let count: number = 0
        while (combatants[new_current_turn].status !== "alive" && count < combatants.length || count === 0) {
             new_current_turn += 1
             // If we've gone through all combatants, increment round and reset turn
            if (new_current_turn >= combatants.length) {
                new_current_turn = 0
                new_round += 1
            }
            count += 1
        }
        if (count === combatants.length && combatants[new_current_turn].status !== "alive") {
            alert("All guys are dead")
            return
        }

        try {
            const payload = { current_turn: new_current_turn, round: new_round }
            //back
            await updateEncounter(encounter_id, payload)
            // Update local state
            setEncounter({ ...encounter, ...payload })
            // Select the next combatant
            setSelectedId(new_current_turn)
        } catch (err) {
            console.error("Failed to advance turn", err);
            alert("Failed to advance turn");
        }
    }

    async function handlePreviousTurn() {
        if (!encounter || !encounter_id) return
        const combatants = encounter.combatants ?? []
        if (combatants.length === 0) return

        let new_current_turn = (encounter.current_turn ?? 0) - 1
        let new_round = encounter.round ?? 1
        // If we've gone before the first combatant, decrement round and go to last combatant
        if (new_current_turn < 0) {
            new_current_turn = combatants.length - 1
            new_round = Math.max(1, new_round - 1)
        }

        try {
            const payload = {current_turn: new_current_turn, round: new_round}
            //back
            await updateEncounter(encounter_id, payload)
            // Update local state
            setEncounter({ ...encounter, ...payload })
            // Select the previous combatant
            setSelectedId(new_current_turn)
        } catch (err) {
            console.error("Failed to go to previous turn", err)
            alert("Failed to go to previous turn")
        }
    }

    async function handleHpChange(
        combatant: Combatant,
        delta: number,
    ){
        if (!encounter || !encounter_id) return

        const newHp = Math.max(
            0,
            Math.min(
                combatant.hit_points_value,
                combatant.current_hp + delta
            )
        )

        try {
            // 1. Сначала обновляем backend
            let new_status: CombatantStatus = "alive"
            if (newHp === 0) { // changing status
                if (combatant.type === "monster") {
                    new_status = "dead"
                }
                else {
                    new_status = "unconscious"
                }
            }
            const updatedCombatant = await updateCombatant(
                encounter_id,
                combatant.combatant_id,
                { current_hp: newHp, status: new_status},
            )
            // 2. Обновляем локальный encounter
            setEncounter(prev => {
                if (!prev) return prev
                return {
                    ...prev,
                    combatants: prev.combatants.map(c =>
                        c.combatant_id === combatant.combatant_id
                            ? {
                                  ...c,
                                  ...updatedCombatant,
                                  current_hp: newHp,
                                  status: new_status,
                              }
                            : c
                    ),
                }
            })
        } catch (err) {
            console.error(
                "Failed to update combatant HP:",
                err
            );
        }
    }

    async function handleStartCombat() {
        try {
            setIsCombatStarted(true)
            setEncounter({...encounter, round: 1, current_turn: 0})
            await updateEncounter(encounter_id, {round: 1, current_turn: 0})
            setSelectedId(0)
        } catch (err) {
            console.error(
                "Failed to start combat:",
                err
            );
        }
    }

    async function handleResetCombat() {
        try {
            const reset_combatants: Combatant[] = encounter.combatants.map((comb: Combatant) => ({
                ...comb,
                current_hp: comb.hit_points_value,
                status: "alive",
            }))
            await Promise.all(
                reset_combatants.map((comb: Combatant) =>
                    updateCombatant(
                        encounter_id,
                        comb.combatant_id,
                        {
                            current_hp: comb.current_hp,
                            status: comb.status,
                        }
                        )
                )
            )
            setIsCombatStarted(false)
            setEncounter({...encounter, combatants: reset_combatants, round: 0, current_turn: 0})
            await updateEncounter(encounter_id, {round: 0, current_turn: 0})
            setSelectedId(0)
        } catch (err) {
            console.error(
                "Failed to reset combat:",
                err
            )
        }
    }

    async function handleRerollAllInitiative() {
        try {
            const reset_combatants: Combatant[] = encounter.combatants.map((comb: Combatant) => ({
                ...comb,
                current_initiative: Math.floor(Math.random() * 20) + 1 + comb.initiative
            }))
            reset_combatants.sort((a, b) => {
                    return(
                        b.current_initiative - a.current_initiative || b.initiative - a.initiative || a.combatant_id.localeCompare(b.combatant_id)
                    )
                })
            await Promise.all(
                reset_combatants.map((comb: Combatant) =>
                    updateCombatant(
                        encounter_id,
                        comb.combatant_id,
                        {
                            current_initiative: comb.current_initiative
                        }
                        )
                )
            )
            setEncounter({...encounter, combatants: reset_combatants})
        } catch (err) {
            console.error(
                "Failed to reroll all initiative:",
                err
            )
        }
    }

    async function handleStatRoll(comb: Combatant, bonus: number) {
        const roll_result = Math.floor(Math.random() * 20) + 1
        setRollResult({
            actor: comb.nickname,
            formula: "1d20 + " + bonus,
            result: roll_result,
            bonus: bonus
        })
    }

        const encounterName = encounter?.name ?? "Encounter"
        const round = encounter?.round ?? 0
        const combatants = encounter?.combatants ?? []
        const historyData = encounter?.history ?? []
        const current_turn = encounter?.current_turn ?? 0
        const selectedCombatant = combatants[selected_id] ?? null

        return (
            <Box
                sx={{
                    width: "100vw",
                    height: "100vh",
                    display: "flex",
                    flexDirection: "column",
                    overflow: "hidden",
                }}
            >
                <Header
                    encounterName={encounterName}
                    round={round}
                    combatStarted={is_combat_started}
                    onStartCombat={handleStartCombat}
                    onResetCombat={handleResetCombat}
                />

                <Box
                    sx={{
                        flex: 1,
                        display: "flex",
                        overflow: "hidden",
                    }}
                >
                    <Sidebar
                        combatants={combatants}
                        selected_id={selected_id}
                        current_turn={combatants.length > 0 ? current_turn : null}
                        onSelect={(id) => setSelectedId(id)}
                        onAddCombatant={handleAddCombatant}
                        onDeleteCombatant={handleDeleteCombatant}
                        onRerollInitiative={handleRerollAllInitiative}
                    />

                    <CombatPanel
                        combatant={selectedCombatant}
                        history={historyData}
                        onHpChange={handleHpChange}
                        onStatRoll={handleStatRoll}
                        onUpdateCombatant={handleUpdateCombatant}
                    />
                </Box>

                {rollResult && (
                    <RollSnackbar
                        open={true}
                        actor={rollResult.actor}
                        formula={rollResult.formula}
                        roll_result={rollResult.result}
                        bonus={rollResult.bonus}
                        onClose={() => setRollResult(null)}
                    />
                )}

                <Footer
                    combatStarted={is_combat_started}
                    onPrevious={handlePreviousTurn}
                    onNext={handleNextTurn}
                    onEndCombat={() => {}}
                />
            </Box>
        );
}