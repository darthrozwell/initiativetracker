import pytest


@pytest.mark.asyncio
async def test_get_combatant(client):
    response = await client.get("/encounter/test_encounter_id/combatant")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_combatant(client):
    response = await client.post("/encounter/test_encounter_id/combatant", json={
                                                                                      "combatant": {
                                                                                        "monster_id": "test_monster_id",
                                                                                        "nickname": "new_comb",
                                                                                        "current_hp": 0,
                                                                                        "current_initiative": 0,
                                                                                        "status": "alive"
                                                                                      }
                                                                                    })
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_create_bad_combatant(client):
    response = await client.post("/encounter/encounter_test_id/combatant", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_update_combatant(client):
    response = await client.put("/encounter/encounter_test_id/combatant/test_combatant_id", json={
                                                                              "combatant": {
                                                                                "monster_id": "test_monster_id",
                                                                                "nickname": "",
                                                                                "current_hp": 20,
                                                                                "status": "alive"
                                                                              }
                                                                            })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_bad_combatant(client):
    response = await client.put("/encounter/encounter_test_id/combatant/test_combatant_id", json = {})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_delete_combatant(client):
    response = await client.delete("/encounter/encounter_test_id/combatant/test_combatant_id")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_fake_combatant(client):
    response = await client.delete("/encounter/encounter_test_id/combatant/fake_combatant_id")
    assert response.status_code == 404
