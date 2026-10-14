from src.domain.models import Order
from src.use_cases.interfaces import IOrderRepository


class InMemoryOrderRepository(IOrderRepository):
    def __init__(self) -> None:
        self._storage: dict[str, Order] = {}

    def save(self, order: Order) -> None:
        self._storage[order.order_id] = order

    def get_by_id(self, order_id: str) -> Order | None:
        return self._storage.get(order_id)

