from fastapi import APIRouter

from src.delivery.api.v1.items.create_router import create_router
from src.delivery.api.v1.items.delete_router import delete_router
from src.delivery.api.v1.items.find_all_router import find_all_router
from src.delivery.api.v1.items.find_one_router import find_one_router
from src.delivery.api.v1.items.update_router import update_router

items_router = APIRouter()


items_router.include_router(create_router)
items_router.include_router(find_all_router)
items_router.include_router(find_one_router)
items_router.include_router(update_router)
items_router.include_router(delete_router)
