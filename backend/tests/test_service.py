# import pytest
#
# from monster.models import MonsterModel
# from monster.schemas import MonsterInSchema
# from monster.service import MonsterService
#
#
# async def test_get_by_name(monster_service: MonsterService):
#     result = await monster_service.get_by_name("test_monster")
#     assert type(result) == MonsterModel
#
#
# async def test_get_all(monster_service: MonsterService):
#     result = await monster_service.get_all()
#     assert type(result) == list[MonsterModel]
#
#
# async def test_add(monster_service: MonsterService):
#     result = await monster_service.add(MonsterInSchema(name="test_monster"))
#     assert type(result) == MonsterModel
#
#
# async def test_update(monster_service: MonsterService):
#     result = await monster_service.update(MonsterInSchema(name="test_monster"))
#     assert type(result) == MonsterModel
#
# async def test_delete(monster_service: MonsterService):
#     result_del = await monster_service.delete(monster_id='test_monster')
#     result = await monster_service.get_by_name(name='test_monster')
#     assert result is None
