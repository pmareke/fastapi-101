from doublex import Mimic, Stub
from expects import equal, expect

from src.domain.item import Item, ItemID
from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.queries.find_all_items_query import FindAllItemsQueryHandler


class TestFindAllItemsQuery:
    def test_find_all_items(self):
        item_id = ItemID()
        item = Item(item_id, name="Item 1", value=10)
        items = [item]
        with Mimic(Stub, DummyItemsRepository) as items_repository:
            items_repository.find_all().returns(items)
        handler = FindAllItemsQueryHandler(items_repository)

        response = handler.execute()

        expect(response.items).to(equal(items))
