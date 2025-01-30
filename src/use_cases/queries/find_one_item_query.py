from dataclasses import dataclass

from src.domain.exceptions import (
    FindOneItemQueryHandlerException,
    ItemNotFoundException,
)
from src.domain.item import Item
from src.domain.items_repository import ItemsRepository


class FindOneItemQueryResponse:
    def __init__(self, item: Item) -> None:
        self.item = item


@dataclass
class FindOneItemQuery:
    name: str


class FindOneItemQueryHandler:
    def __init__(self, items_repository: ItemsRepository) -> None:
        self.items_repository = items_repository

    def execute(self, query: FindOneItemQuery) -> FindOneItemQueryResponse:
        try:
            items = self.items_repository.find(query.name)
            return FindOneItemQueryResponse(items)
        except ItemNotFoundException as ex:
            raise FindOneItemQueryHandlerException from ex
