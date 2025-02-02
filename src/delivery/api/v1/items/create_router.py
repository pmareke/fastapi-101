from http.client import CREATED

from fastapi import APIRouter, Depends

from src.delivery.api.v1.items.item_request import ItemRequest
from src.domain.item import Item, ItemID
from src.infrastructure.dummy_items_repository import DummyItemsRepositoryFactory
from src.use_cases.commands.create_one_item_command import (
    CreateOneItemCommand,
    CreateOneItemCommandHandler,
)

create_router = APIRouter()


def _get_handler():
    items_repository = DummyItemsRepositoryFactory.create()
    return CreateOneItemCommandHandler(items_repository)


@create_router.post("/", status_code=CREATED)
def create_one_item(
    item_request: ItemRequest,
    handler: CreateOneItemCommandHandler = Depends(_get_handler),
) -> ItemID:
    item = Item(name=item_request.name, value=item_request.value)
    command = CreateOneItemCommand(item)
    response = handler.execute(command)
    return response.item_id
