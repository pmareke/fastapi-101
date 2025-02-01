from src.domain.item import ItemID


class ItemNotFoundException(Exception):
    def __init__(self, item_id: ItemID):
        super().__init__(f"Item with id {item_id.id} not found")


class FindOneItemQueryHandlerException(Exception):
    pass


class DeleteOneItemQueryHandlerException(Exception):
    pass
