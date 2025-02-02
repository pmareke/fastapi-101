from src.domain.exceptions import ItemNotFoundException
from src.domain.item import Item, ItemID
from src.domain.items_repository import ItemsRepository


class DummyItemsRepository(ItemsRepository):
    def __init__(self):
        self.items: dict[ItemID, Item] = {}

    def find_all(self) -> list[Item]:
        return list(self.items.values())

    def find(self, item_id: ItemID) -> Item:
        try:
            return self.items[item_id]
        except KeyError:
            raise ItemNotFoundException(item_id)

    def save(self, item: Item) -> ItemID:
        self.items[item.id] = item
        return item.id

    def update(self, item_id: ItemID, item: Item) -> None:
        self.items[item_id] = item

    def delete(self, item_id: ItemID) -> None:
        try:
            del self.items[item_id]
        except KeyError:
            raise ItemNotFoundException(item_id)


class DummyItemsRepositoryFactory:
    repository: DummyItemsRepository | None = None

    @classmethod
    def create(cls) -> DummyItemsRepository:
        if not cls.repository:
            cls.repository = DummyItemsRepository()
        return cls.repository
