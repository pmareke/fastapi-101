from fastapi import APIRouter, Depends

from src.domain.item import Item
from src.infrastructure.dummy_items_repository import DummyItemsRepositoryFactory
from src.use_cases.queries.find_all_items_query import FindAllItemsQueryHandler

find_all_router = APIRouter()


def _get_find_all_items_handler():
    items_repository = DummyItemsRepositoryFactory.create()
    return FindAllItemsQueryHandler(items_repository)


@find_all_router.get("/")
def find_all_items(
    handler: FindAllItemsQueryHandler = Depends(_get_find_all_items_handler),
) -> list[Item]:
    response = handler.execute()
    return response.items
