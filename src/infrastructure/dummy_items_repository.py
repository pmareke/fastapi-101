from src.domain.exceptions import ItemNotFoundException
from src.domain.item import Item


class DummyItemsRepository:
    def __init__(self):
        self.items = {}

    def find_all(self) -> list[Item]:
        return list(self.items.values())

    def find(self, item_id: str) -> Item:
        try:
            return self.items[item_id]
        except KeyError:
            raise ItemNotFoundException(f"Item with id {item_id} not found")

    def save(self, item: Item) -> None:
        self.items["name"] = item

    def update(self, item_id: str, item: Item) -> None:
        self.items[item_id] = item

    def delete(self, item_id: str) -> None:
        try:
            del self.items[item_id]
        except KeyError:
            raise ItemNotFoundException(f"Item with id {item_id} not found")
