import pytest


@pytest.mark.asyncio
async def test_get_encounter(client):
    response = await client.get("/encounter/test_encounter_id")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_encounter_fake(client):
    response = await client.get("/encounter/test_encounter_fake_id")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_all_encounters(client):
    response = await client.get("/encounter/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_add_encounter(client):
    response = await client.post("/encounter/", json = {
                                                          "encounter": {
                                                            "name": "string",
                                                            "round": 1,
                                                            "current_turn": 0
                                                          }
                                    })
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_add_bad_encounter(client):
    response = await client.post("/encounter/", json = {})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_update_encounter(client):
    response = await client.put("/encounter/test_encounter_id", json = {
                                                                          "encounter": {
                                                                            "name": "updated_test_name",
                                                                            "round": 1,
                                                                            "current_turn": 0
                                                                          }
                                                                        })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_bad_encounter(client):
    response = await client.put("/encounter/test_encounter_id", json = {})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_delete_encounter(client):
    response = await client.delete("/encounter/test_encounter_id")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_bad_encounter(client):
    response = await client.delete("/encounter/test_encounter_fake_id")
    assert response.status_code == 404
