from abc import ABC, abstractmethod

from src.domain.item import Item


class ItemsRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Item]:
        raise NotImplementedError

    @abstractmethod
    def find(self, item_id: str) -> Item:
        raise NotImplementedError

    @abstractmethod
    def save(self, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, item_id: str, item: Item) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: str) -> None:
        raise NotImplementedError
