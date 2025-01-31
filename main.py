from fastapi import FastAPI

from src.delivery.api.v1.items.items_router import items_router

app = FastAPI()

app.include_router(prefix="/api/v1/items", router=items_router)
