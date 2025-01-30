from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.domain.item import Item
from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.commands.create_new_item_command import (
    CreateOneItemCommand,
    CreateOneItemCommandHandler,
)


class TestCreateOneItemCommand:
    def test_create_one_item(self):
        item = Item(name="Item 1", value=10)
        items_repository = Mimic(Spy, DummyItemsRepository)
        command = CreateOneItemCommand(item)
        handler = CreateOneItemCommandHandler(items_repository)

        handler.execute(command)

        expect(items_repository.save).to(have_been_called_with(item))
