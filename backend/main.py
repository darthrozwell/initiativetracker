from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.monster_router import router as monster_router
from api.v1.encounter_router import router as encounter_router
from database_core import setup_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    await setup_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(monster_router)
app.include_router(encounter_router)
