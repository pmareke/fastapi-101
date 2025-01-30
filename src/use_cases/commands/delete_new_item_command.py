from dataclasses import dataclass

from src.domain.exceptions import (
    DeleteOneItemQueryHandlerException,
    ItemNotFoundException,
)
from src.domain.items_repository import ItemsRepository


@dataclass
class DeleteOneItemCommand:
    name: str


class DeleteOneItemCommandHandler:
    def __init__(self, items_repository: ItemsRepository) -> None:
        self.items_repository = items_repository

    def execute(self, command: DeleteOneItemCommand) -> None:
        try:
            self.items_repository.delete(command.name)
        except ItemNotFoundException as ex:
            raise DeleteOneItemQueryHandlerException from ex
