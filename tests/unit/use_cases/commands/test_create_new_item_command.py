from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.commands.create_new_item_command import (
    CreateOneItemCommand,
    CreateOneItemCommandHandler,
)
from tests.builders.item_builder import ItemBuilder


class TestCreateOneItemCommand:
    def test_create_one_item(self):
        item = ItemBuilder().build()
        items_repository = Mimic(Spy, DummyItemsRepository)
        command = CreateOneItemCommand(item)
        handler = CreateOneItemCommandHandler(items_repository)

        handler.execute(command)

        expect(items_repository.save).to(have_been_called_with(item))
