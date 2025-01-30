from dataclasses import dataclass


@dataclass
class ItemRequest:
    name: str
    value: float
