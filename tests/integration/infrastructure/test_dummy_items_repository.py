from expects import be_empty, equal, expect, raise_error

from src.domain.exceptions import ItemNotFoundException
from src.domain.item import Item
from src.integration.dummy_items_repository import DummyItemsRepository


class TestDummyItemsRepository:
    def test_save(self) -> None:
        repository = DummyItemsRepository()
        item = Item("name", 100)

        repository.save(item)
        items = repository.find_all()

        expect(items).to(equal([item]))

    def test_find_all(self) -> None:
        repository = DummyItemsRepository()

        items = repository.find_all()

        expect(items).to(be_empty)

    def test_find(self) -> None:
        repository = DummyItemsRepository()
        item = Item("name", 100)

        repository.save(item)
        found_item = repository.find("name")

        expect(found_item).to(equal(item))

    def test_raise_exception_finding_a_non_existing_item(self) -> None:
        repository = DummyItemsRepository()

        expect(lambda: repository.find("name")).to(raise_error(ItemNotFoundException))

    def test_update(self) -> None:
        repository = DummyItemsRepository()
        item = Item("name", 100)

        repository.update("name", item)
        item = repository.find("name")

        expect(item).to(equal(item))

    def test_delete(self) -> None:
        repository = DummyItemsRepository()
        item = Item("name", 100)

        repository.save(item)
        repository.delete("name")
        items = repository.find_all()

        expect(items).to(be_empty)

    def test_raise_exception_deleting_a_non_existing_item(self) -> None:
        repository = DummyItemsRepository()

        expect(lambda: repository.delete("name")).to(raise_error(ItemNotFoundException))
