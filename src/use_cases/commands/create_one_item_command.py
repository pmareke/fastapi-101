from dataclasses import dataclass

from src.domain.item import Item, ItemID
from src.domain.items_repository import ItemsRepository


class CreateOneItemCommandResponse:
    def __init__(self, item_id: ItemID) -> None:
        self.item_id = item_id


@dataclass
class CreateOneItemCommand:
    item: Item


class CreateOneItemCommandHandler:
    def __init__(self, items_repository: ItemsRepository) -> None:
        self.items_repository = items_repository

    def execute(self, command: CreateOneItemCommand) -> CreateOneItemCommandResponse:
        item_id = self.items_repository.save(command.item)
        return CreateOneItemCommandResponse(item_id)
