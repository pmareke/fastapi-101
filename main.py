from contextlib import asynccontextmanager
from time import sleep
from typing import AsyncGenerator

from fastapi import FastAPI

from src.delivery.api.v1.items.items_router import items_router


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    print("Starting up")
    yield

    sleep(5)
    print("Shutting down")


app = FastAPI(lifespan=lifespan)

app.include_router(prefix="/api/v1/items", router=items_router)
