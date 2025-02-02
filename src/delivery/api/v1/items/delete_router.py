from http.client import NO_CONTENT, NOT_FOUND

from fastapi import APIRouter, Depends, HTTPException

from src.domain.exceptions import (
    DeleteOneItemQueryHandlerException,
)
from src.domain.item import ItemID
from src.infrastructure.dummy_items_repository import DummyItemsRepositoryFactory
from src.use_cases.commands.delete_one_item_command import (
    DeleteOneItemCommand,
    DeleteOneItemCommandHandler,
)

delete_router = APIRouter()


def _get_delete_one_item_handler():
    items_repository = DummyItemsRepositoryFactory.create()
    return DeleteOneItemCommandHandler(items_repository)


@delete_router.delete("/{item_id}", status_code=NO_CONTENT)
def delete_one_item(
    item_id: str,
    handler: DeleteOneItemCommandHandler = Depends(_get_delete_one_item_handler),
) -> None:
    try:
        command = DeleteOneItemCommand(ItemID(item_id))
        handler.execute(command)
    except DeleteOneItemQueryHandlerException as ex:
        raise HTTPException(status_code=NOT_FOUND, detail=str(ex)) from ex
