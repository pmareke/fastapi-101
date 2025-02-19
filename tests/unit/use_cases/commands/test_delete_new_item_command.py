from doublex import Mimic, Spy, Stub
from doublex_expects import have_been_called_with
from expects import expect, raise_error

from src.domain.exceptions import (
    DeleteOneItemCommandHandlerException,
    ItemNotFoundException,
)
from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.commands.delete_one_item_command import (
    DeleteOneItemCommand,
    DeleteOneItemCommandHandler,
)
from tests.builders.item_builder import ItemBuilder


class TestDeleteOneItemsCommand:
    def test_delete_one_item(self):
        item = ItemBuilder().build()
        items_repository = Mimic(Spy, DummyItemsRepository)
        command = DeleteOneItemCommand(item.id)
        handler = DeleteOneItemCommandHandler(items_repository)

        handler.execute(command)

        expect(items_repository.delete).to(have_been_called_with(item.id))

    def test_raise_exception_when_deleting_a_non_existing_item(self):
        item = ItemBuilder().build()
        with Mimic(Stub, DummyItemsRepository) as items_repository:
            items_repository.delete(item.id).raises(ItemNotFoundException(item.id))
        query = DeleteOneItemCommand(item.id)
        handler = DeleteOneItemCommandHandler(items_repository)

        expect(lambda: handler.execute(query)).to(
            raise_error(DeleteOneItemCommandHandlerException)
        )
