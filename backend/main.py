from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.router import router
from database_core import setup_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    await setup_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)