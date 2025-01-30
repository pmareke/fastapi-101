from expects import be_empty, equal, expect, raise_error

from src.domain.exceptions import ItemNotFoundException
from src.domain.item import Item, ItemID
from src.infrastructure.dummy_items_repository import DummyItemsRepository
from tests.builders.item_builder import ItemBuilder


class TestDummyItemsRepository:
    def test_save(self) -> None:
        repository = DummyItemsRepository()
        item = ItemBuilder().build()

        repository.save(item)
        items = repository.find_all()

        expect(items).to(equal([item]))

    def test_find_all(self) -> None:
        repository = DummyItemsRepository()

        items = repository.find_all()

        expect(items).to(be_empty)

    def test_find(self) -> None:
        repository = DummyItemsRepository()
        item = ItemBuilder().build()

        repository.save(item)
        found_item = repository.find(item.item_id)

        expect(found_item).to(equal(item))

    def test_raise_exception_finding_a_non_existing_item(self) -> None:
        repository = DummyItemsRepository()
        item_id = ItemID("non-existing")

        expect(lambda: repository.find(item_id)).to(raise_error(ItemNotFoundException))

    def test_update(self) -> None:
        repository = DummyItemsRepository()
        item = ItemBuilder().build()

        repository.update(item.item_id, item)
        item = repository.find(item.item_id)

        expect(item).to(equal(item))

    def test_delete(self) -> None:
        repository = DummyItemsRepository()
        item = ItemBuilder().build()

        id = repository.save(item)
        repository.delete(id)
        items = repository.find_all()

        expect(items).to(be_empty)

    def test_raise_exception_deleting_a_non_existing_item(self) -> None:
        item_id = ItemID("non-existing")
        repository = DummyItemsRepository()

        expect(lambda: repository.delete(item_id)).to(
            raise_error(ItemNotFoundException)
        )
