from src.domain.item import Item
from src.domain.items_repository import ItemsRepository


class FindAllItemsQueryResponse:
    def __init__(self, items: list[Item]) -> None:
        self.items = items


class FindAllItemsQueryHandler:
    def __init__(self, items_repository: ItemsRepository) -> None:
        self.items_repository = items_repository

    def execute(self):
        items = self.items_repository.find_all()
        return FindAllItemsQueryResponse(items)
