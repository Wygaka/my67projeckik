from abc import ABC, abstractmethod

from src.domain.models import Order


class IOrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order | None:
        raise NotImplementedError

