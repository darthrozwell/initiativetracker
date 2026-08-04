from pydantic import BaseModel, Field


class BaseMonster(BaseModel):
    pass

class Monster(BaseMonster):
    name: str = Field(min_length=1, max_length=50)
