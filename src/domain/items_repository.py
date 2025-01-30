from abc import ABC, abstractmethod

from src.domain.item import Item, ItemID


class ItemsRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Item]:
        raise NotImplementedError

    @abstractmethod
    def find(self, item_id: ItemID) -> Item:
        raise NotImplementedError

    @abstractmethod
    def save(self, item: Item) -> ItemID:
        raise NotImplementedError

    @abstractmethod
    def update(self, item_id: ItemID, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: ItemID) -> None:
        raise NotImplementedError
