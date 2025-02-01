from http.client import CREATED, NO_CONTENT, NOT_FOUND

from fastapi import APIRouter, Depends, HTTPException

from src.delivery.api.v1.items.item_request import ItemRequest
from src.domain.exceptions import (
    DeleteOneItemQueryHandlerException,
    FindOneItemQueryHandlerException,
)
from src.domain.item import Item, ItemID
from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.commands.create_one_item_command import (
    CreateOneItemCommand,
    CreateOneItemCommandHandler,
)
from src.use_cases.commands.delete_one_item_command import (
    DeleteOneItemCommand,
    DeleteOneItemCommandHandler,
)
from src.use_cases.commands.update_one_item_command import (
    UpdateOneItemCommand,
    UpdateOneItemCommandHandler,
)
from src.use_cases.queries.find_all_items_query import FindAllItemsQueryHandler
from src.use_cases.queries.find_one_item_query import (
    FindOneItemQuery,
    FindOneItemQueryHandler,
)

items_router = APIRouter()

items_repository = DummyItemsRepository()


def _get_create_one_item_handler():
    return CreateOneItemCommandHandler(items_repository)


@items_router.post("/", status_code=CREATED)
def create_one_item(
    item_request: ItemRequest,
    handler: CreateOneItemCommandHandler = Depends(_get_create_one_item_handler),
) -> ItemID:
    item = Item(item_request.name, item_request.value)
    command = CreateOneItemCommand(item)
    response = handler.execute(command)
    return response.item_id


def _get_find_all_items_handler():
    return FindAllItemsQueryHandler(items_repository)


@items_router.get("/")
def find_all_items(
    handler: FindAllItemsQueryHandler = Depends(_get_find_all_items_handler),
) -> list[Item]:
    response = handler.execute()
    return response.items


def _get_find_one_item_handler():
    return FindOneItemQueryHandler(items_repository)


@items_router.get("/{item_id}")
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


def _get_update_one_item_handler():
    return UpdateOneItemCommandHandler(items_repository)


@items_router.put("/{id}")
def update_one_item(
    id: str,
    item_request: ItemRequest,
    handler: UpdateOneItemCommandHandler = Depends(_get_update_one_item_handler),
) -> None:
    item_id = ItemID(id)
    item = Item(item_request.name, item_request.value, item_id)
    command = UpdateOneItemCommand(item)
    handler.execute(command)


def _get_delete_one_item_handler():
    return DeleteOneItemCommandHandler(items_repository)


@items_router.delete("/{item_id}", status_code=NO_CONTENT)
def delete_one_item(
    item_id: str,
    handler: DeleteOneItemCommandHandler = Depends(_get_delete_one_item_handler),
) -> None:
    try:
        command = DeleteOneItemCommand(ItemID(item_id))
        handler.execute(command)
    except DeleteOneItemQueryHandlerException as ex:
        raise HTTPException(status_code=NOT_FOUND, detail=str(ex)) from ex
