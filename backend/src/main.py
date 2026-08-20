from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.monster.router import router as monster_router
from src.encounter.router import router as encounter_router
from src.character.router import router as player_router



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=monster_router, prefix="/monster", tags=["monsters"])
app.include_router(router=encounter_router, prefix="/encounter", tags=["encounters"])
app.include_router(router=player_router, prefix="/character", tags=["characters"])
