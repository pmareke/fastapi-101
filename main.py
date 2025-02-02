from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from time import sleep

from fastapi import FastAPI

from src.delivery.api.v1.items.items_router import items_router


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    yield
    sleep(5)  # Graceful shutdown


app = FastAPI(lifespan=lifespan)


app.include_router(prefix="/api/v1/items", router=items_router)
