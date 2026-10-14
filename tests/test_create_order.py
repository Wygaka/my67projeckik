import tempfile
import unittest
from pathlib import Path

from src.infrastructure.memory_repo import InMemoryOrderRepository
from src.infrastructure.sqlite_repo import SqliteOrderRepository
from src.use_cases.create_order import CreateOrderUseCase


class TestCreateOrderUseCase(unittest.TestCase):
    def test_create_order_saves_to_memory_repository(self) -> None:
        repository = InMemoryOrderRepository()
        use_case = CreateOrderUseCase(repository)

        result = use_case.execute(
            "ORD-100",
            [
                {"id": "1", "title": "Router", "price": 3000, "quantity": 1},
                {"id": "2", "title": "Cable", "price": 1000, "quantity": 3},
            ],
        )

        self.assertEqual(result["subtotal"], 6000.0)
        self.assertEqual(result["discount"], 600.0)
        self.assertEqual(result["final_amount"], 5400.0)
        self.assertIsNotNone(repository.get_by_id("ORD-100"))

    def test_sqlite_repository_restores_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = SqliteOrderRepository(Path(directory) / "orders.db")
            use_case = CreateOrderUseCase(repository)

            use_case.execute(
                "ORD-200",
                [{"id": "1", "title": "Notebook", "price": 2500, "quantity": 2}],
            )

            restored = repository.get_by_id("ORD-200")
            self.assertIsNotNone(restored)
            self.assertEqual(restored.calculate_final_amount(), 4500.0)


if __name__ == "__main__":
    unittest.main()

