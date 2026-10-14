from pathlib import Path

from src.infrastructure.logging_middleware import LoggingCreateOrderMiddleware
from src.infrastructure.sqlite_repo import SqliteOrderRepository
from src.use_cases.create_order import CreateOrderUseCase


def build_create_order_use_case() -> LoggingCreateOrderMiddleware:
    database_path = Path(__file__).resolve().parent.parent / "orders.db"
    repository = SqliteOrderRepository(database_path)
    use_case = CreateOrderUseCase(repository)
    return LoggingCreateOrderMiddleware(use_case)


def main() -> None:
    create_order = build_create_order_use_case()
    result = create_order.execute(
        order_id="ORD-001",
        raw_items=[
            {"id": "ITM-001", "title": "Server Rack", "price": 4000.0, "quantity": 1},
            {"id": "ITM-002", "title": "Patch Cord", "price": 1500.0, "quantity": 1},
        ],
    )
    print(result)


if __name__ == "__main__":
    main()

