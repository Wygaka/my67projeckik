from dataclasses import dataclass
from typing import Iterable


DISCOUNT_THRESHOLD = 5000.0
DISCOUNT_RATE = 0.10


@dataclass(frozen=True)
class OrderItem:
    item_id: str
    title: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if not self.item_id.strip():
            raise ValueError("Item id must not be empty.")
        if not self.title.strip():
            raise ValueError("Item title must not be empty.")
        if self.price < 0:
            raise ValueError("Item price must not be negative.")
        if self.quantity <= 0:
            raise ValueError("Item quantity must be positive.")

    @property
    def total_price(self) -> float:
        return round(self.price * self.quantity, 2)


class Order:
    def __init__(self, order_id: str, items: Iterable[OrderItem]):
        materialized_items = list(items)
        if not order_id.strip():
            raise ValueError("Order id must not be empty.")
        if not materialized_items:
            raise ValueError("Order must contain at least one item.")

        self.order_id = order_id
        self._items = tuple(materialized_items)

    @property
    def items(self) -> tuple[OrderItem, ...]:
        return self._items

    def calculate_subtotal(self) -> float:
        return round(sum(item.total_price for item in self._items), 2)

    def calculate_discount(self) -> float:
        subtotal = self.calculate_subtotal()
        if subtotal >= DISCOUNT_THRESHOLD:
            return round(subtotal * DISCOUNT_RATE, 2)
        return 0.0

    def calculate_final_amount(self) -> float:
        return round(self.calculate_subtotal() - self.calculate_discount(), 2)

