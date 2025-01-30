from src.domain.item import Item, ItemID


class ItemBuilder:
    def __init__(self):
        self.item_id = ItemID()
        self.name = "Item Name"
        self.value = 100

    def with_item_id(self, item_id: ItemID) -> "ItemBuilder":
        self.item_id = item_id
        return self

    def with_name(self, name: str) -> "ItemBuilder":
        self.name = name
        return self

    def with_value(self, value: int) -> "ItemBuilder":
        self.value = value
        return self

    def build(self) -> Item:
        return Item(
            self.item_id,
            self.name,
            self.value,
        )
