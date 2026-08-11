import pytest


@pytest.mark.asyncio
async def test_create_monster(client):
    response = await client.post("/monster/", json={
                                                      "monster": {
                                                        "name": "string2",
                                                        "source": "Custom",
                                                        "size": "Средний",
                                                        "creature_type": "Гуманоид",
                                                        "alignment": "Нейтральный",
                                                        "armor_class": 1,
                                                        "initiative": 1,
                                                        "hit_points_value": 1,
                                                        "hit_points_formula": "string",
                                                        "speed": "string",
                                                        "skills": "string",
                                                        "damage_resistance": "string",
                                                        "damage_immunity": "string",
                                                        "damage_vulnerability": "string",
                                                        "senses": "string",
                                                        "languages": "string",
                                                        "challenge_rating": "string",
                                                        "experience": 1,
                                                        "proficiency_bonus": 1,
                                                        "equipment": "string",
                                                        "treasure": "string",
                                                        "habitat": "string",
                                                        "strength_value": 10,
                                                        "strength_mod": 0,
                                                        "strength_save": 0,
                                                        "dexterity_value": 10,
                                                        "dexterity_mod": 0,
                                                        "dexterity_save": 0,
                                                        "constitution_value": 10,
                                                        "constitution_mod": 0,
                                                        "constitution_save": 0,
                                                        "intelligence_value": 10,
                                                        "intelligence_mod": 0,
                                                        "intelligence_save": 0,
                                                        "wisdom_value": 10,
                                                        "wisdom_mod": 0,
                                                        "wisdom_save": 0,
                                                        "charisma_value": 10,
                                                        "charisma_mod": 0,
                                                        "charisma_save": 0,
                                                        "abilities": [
                                                          {
                                                            "title": "",
                                                            "name": "",
                                                            "text": "",
                                                            "attack_type": "",
                                                            "attack_range": "",
                                                            "hit_bonus": 0,
                                                            "reach": "",
                                                            "damage": ""
                                                          }
                                                        ]
                                                      }
                                                    })
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_create_monster_bad_data(client):
    response = await client.post("/monster/", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_monster(client):
    response = await client.get("/monster/test_monster_name")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_not_existing_monster(client):
    response = await client.get("/monster/test_monster_fake_name")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_all_monsters(client):
    response = await client.get("/monster/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_monster(client):
    response = await client.put("/monster/test_monster_name", json={
                                                      "monster": {
                                                        "monster_id": "test_monster_id",
                                                        "name": "test_monster_name",
                                                        "source": "Custom",
                                                        "size": "Средний",
                                                        "creature_type": "Гуманоид",
                                                        "alignment": "Нейтральный",
                                                        "armor_class": 12, #updated
                                                        "initiative": 1,
                                                        "hit_points_value": 1,
                                                        "hit_points_formula": "string",
                                                        "speed": "string",
                                                        "skills": "string",
                                                        "damage_resistance": "string",
                                                        "damage_immunity": "string",
                                                        "damage_vulnerability": "string",
                                                        "senses": "string",
                                                        "languages": "string",
                                                        "challenge_rating": "string",
                                                        "experience": 1,
                                                        "proficiency_bonus": 1,
                                                        "equipment": "string",
                                                        "treasure": "string",
                                                        "habitat": "string",
                                                        "strength_value": 10,
                                                        "strength_mod": 0,
                                                        "strength_save": 0,
                                                        "dexterity_value": 10,
                                                        "dexterity_mod": 0,
                                                        "dexterity_save": 0,
                                                        "constitution_value": 10,
                                                        "constitution_mod": 0,
                                                        "constitution_save": 0,
                                                        "intelligence_value": 10,
                                                        "intelligence_mod": 0,
                                                        "intelligence_save": 0,
                                                        "wisdom_value": 10,
                                                        "wisdom_mod": 0,
                                                        "wisdom_save": 0,
                                                        "charisma_value": 10,
                                                        "charisma_mod": 0,
                                                        "charisma_save": 0,
                                                        "abilities": [
                                                          {
                                                            "title": "",
                                                            "name": "",
                                                            "text": "",
                                                            "attack_type": "",
                                                            "attack_range": "",
                                                            "hit_bonus": 0,
                                                            "reach": "",
                                                            "damage": ""
                                                          }
                                                        ]
                                                      }
                                                    })
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_monster_bad_data(client):
    response = await client.put("/monster/test_monster_name", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_delete_monster(client):
    response = await client.delete("/monster/test_monster_id")
    assert response.status_code == 204

@pytest.mark.asyncio
async def test_delete_monster_not_found(client):
    response = await client.delete("/monster/test_monster_id2")
    assert response.status_code == 404
