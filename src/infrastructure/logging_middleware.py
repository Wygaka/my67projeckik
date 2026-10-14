from collections.abc import Iterable
from time import perf_counter
from typing import Any, Protocol


class OrderCreationUseCase(Protocol):
    def execute(self, order_id: str, raw_items: Iterable[dict[str, Any]]) -> dict[str, float | str]:
        ...


class LoggingCreateOrderMiddleware:
    def __init__(self, wrapped: OrderCreationUseCase) -> None:
        self._wrapped = wrapped

    def execute(self, order_id: str, raw_items: Iterable[dict[str, Any]]) -> dict[str, float | str]:
        started_at = perf_counter()
        result = self._wrapped.execute(order_id, raw_items)
        elapsed_ms = (perf_counter() - started_at) * 1000
        print(f"create_order completed order_id={order_id} elapsed_ms={elapsed_ms:.2f}")
        return result

