from doublex import Mimic, Spy
from doublex_expects import have_been_called_with
from expects import expect

from src.infrastructure.dummy_items_repository import DummyItemsRepository
from src.use_cases.commands.update_new_item_command import (
    UpdateOneItemCommand,
    UpdateOneItemCommandHandler,
)
from tests.builders.item_builder import ItemBuilder


class TestUpdateItemCommand:
    def test_update_one_item(self):
        item = ItemBuilder().build()
        items_repository = Mimic(Spy, DummyItemsRepository)
        command = UpdateOneItemCommand(item)
        handler = UpdateOneItemCommandHandler(items_repository)

        handler.execute(command)

        expect(items_repository.update).to(have_been_called_with(item.item_id, item))
