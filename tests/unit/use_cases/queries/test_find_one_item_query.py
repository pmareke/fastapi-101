from doublex import Mimic, Stub
from expects import equal, expect, raise_error

from src.domain.exceptions import (
    FindOneItemQueryHandlerException,
    ItemNotFoundException,
)
from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.queries.find_one_item_query import (
    FindOneItemQuery,
    FindOneItemQueryHandler,
)
from tests.builders.item_builder import ItemBuilder


class TestFindOneItemsQuery:
    def test_find_one_item(self):
        item = ItemBuilder().build()
        with Mimic(Stub, DummyItemsRepository) as items_repository:
            items_repository.find(item.id).returns(item)
        query = FindOneItemQuery(item.id)
        handler = FindOneItemQueryHandler(items_repository)

        response = handler.execute(query)

        expect(response.item).to(equal(item))

    def test_raise_exception_when_finding_a_non_existing_item(self):
        item = ItemBuilder().build()
        with Mimic(Stub, DummyItemsRepository) as items_repository:
            items_repository.find(item.id).raises(ItemNotFoundException(item.id))
        query = FindOneItemQuery(item.id)
        handler = FindOneItemQueryHandler(items_repository)

        expect(lambda: handler.execute(query)).to(
            raise_error(FindOneItemQueryHandlerException)
        )
