from dataclasses import dataclass

from src.domain.item import Item
from src.domain.items_repository import ItemsRepository


@dataclass
class UpdateOneItemCommand:
    item: Item


class UpdateOneItemCommandHandler:
    def __init__(self, items_repository: ItemsRepository) -> None:
        self.items_repository = items_repository

    def execute(self, command: UpdateOneItemCommand) -> None:
        self.items_repository.update(command.item.item_id, command.item)
