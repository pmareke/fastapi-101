from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class ItemID:
    value: str = uuid4().hex


@dataclass
class Item:
    item_id: ItemID
    name: str
    value: float
