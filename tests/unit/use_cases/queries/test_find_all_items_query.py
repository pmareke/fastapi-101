from doublex import Mimic, Stub
from expects import equal, expect

from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.queries.find_all_items_query import FindAllItemsQueryHandler
from tests.builders.item_builder import ItemBuilder


class TestFindAllItemsQuery:
    def test_find_all_items(self):
        item = ItemBuilder().build()
        items = [item]
        with Mimic(Stub, DummyItemsRepository) as items_repository:
            items_repository.find_all().returns(items)
        handler = FindAllItemsQueryHandler(items_repository)

        response = handler.execute()

        expect(response.items).to(equal(items))
