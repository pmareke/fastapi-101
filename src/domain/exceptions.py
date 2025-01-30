class ItemNotFoundException(Exception):
    def __init__(self, item_id: str):
        super().__init__(f"Item with id {item_id} not found")


class FindOneItemQueryHandlerException(Exception):
    pass


class DeleteOneItemQueryHandlerException(Exception):
    pass
