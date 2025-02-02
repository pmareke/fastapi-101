from http.client import NOT_FOUND

from fastapi import APIRouter, Depends, HTTPException

from src.domain.exceptions import (
    FindOneItemQueryHandlerException,
)
from src.domain.item import Item, ItemID
from src.infrastructure.dummy_items_repository import DummyItemsRepositoryFactory
from src.use_cases.queries.find_one_item_query import (
    FindOneItemQuery,
    FindOneItemQueryHandler,
)

find_one_router = APIRouter()


def _get_find_one_item_handler():
    items_repository = DummyItemsRepositoryFactory.create()
    return FindOneItemQueryHandler(items_repository)


@find_one_router.get("/{item_id}")
def find_one_item(
    item_id: str,
    handler: FindOneItemQueryHandler = Depends(_get_find_one_item_handler),
) -> Item:
    try:
        query = FindOneItemQuery(ItemID(item_id))
        response = handler.execute(query)
        return response.item
    except FindOneItemQueryHandlerException as ex:
        raise HTTPException(status_code=NOT_FOUND, detail=str(ex))
