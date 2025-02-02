from fastapi import APIRouter, Depends

from src.delivery.api.v1.items.item_request import ItemRequest
from src.domain.item import Item, ItemID
from src.infrastructure.dummy_items_repository import DummyItemsRepositoryFactory
from src.use_cases.commands.update_one_item_command import (
    UpdateOneItemCommand,
    UpdateOneItemCommandHandler,
)

update_router = APIRouter()


def _get_handler():
    items_repository = DummyItemsRepositoryFactory.create()
    return UpdateOneItemCommandHandler(items_repository)


@update_router.put("/{item_id}")
def update_item(
    item_id: str,
    item_request: ItemRequest,
    handler: UpdateOneItemCommandHandler = Depends(_get_handler),
) -> None:
    id = ItemID(item_id)
    item = Item(item_request.name, item_request.value, id)
    command = UpdateOneItemCommand(item)
    handler.execute(command)
