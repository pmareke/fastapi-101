from dataclasses import dataclass

from src.domain.item import Item, ItemID
from src.domain.items_repository import ItemsRepository


@dataclass
class CreateOneItemCommand:
    item: Item


class CreateOneItemCommandHandler:
    def __init__(self, items_repository: ItemsRepository) -> None:
        self.items_repository = items_repository

    def execute(self, command: CreateOneItemCommand) -> ItemID:
        return self.items_repository.save(command.item)
