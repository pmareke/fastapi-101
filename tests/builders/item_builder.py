from src.domain.item import Item


class ItemBuilder:
    def __init__(self):
        self.name = "Item Name"
        self.value = 100

    def with_name(self, name: str) -> "ItemBuilder":
        self.name = name
        return self

    def with_value(self, value: int) -> "ItemBuilder":
        self.value = value
        return self

    def build(self) -> Item:
        return Item(self.name, self.value)
