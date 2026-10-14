import json
import sqlite3
from contextlib import closing
from pathlib import Path

from src.domain.models import Order, OrderItem
from src.use_cases.interfaces import IOrderRepository


class SqliteOrderRepository(IOrderRepository):
    def __init__(self, database_path: str | Path = "orders.db") -> None:
        self._database_path = Path(database_path)
        self._initialize_schema()

    def save(self, order: Order) -> None:
        payload = json.dumps(
            [
                {
                    "id": item.item_id,
                    "title": item.title,
                    "price": item.price,
                    "quantity": item.quantity,
                }
                for item in order.items
            ],
            ensure_ascii=False,
        )
        with closing(sqlite3.connect(self._database_path)) as connection:
            with connection:
                connection.execute(
                    """
                    INSERT INTO orders(order_id, items_json, subtotal, discount, final_amount)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(order_id) DO UPDATE SET
                        items_json = excluded.items_json,
                        subtotal = excluded.subtotal,
                        discount = excluded.discount,
                        final_amount = excluded.final_amount
                    """,
                    (
                        order.order_id,
                        payload,
                        order.calculate_subtotal(),
                        order.calculate_discount(),
                        order.calculate_final_amount(),
                    ),
                )

    def get_by_id(self, order_id: str) -> Order | None:
        with closing(sqlite3.connect(self._database_path)) as connection:
            row = connection.execute(
                "SELECT items_json FROM orders WHERE order_id = ?",
                (order_id,),
            ).fetchone()
        if row is None:
            return None

        items = [
            OrderItem(
                item_id=str(item["id"]),
                title=str(item["title"]),
                price=float(item["price"]),
                quantity=int(item["quantity"]),
            )
            for item in json.loads(row[0])
        ]
        return Order(order_id=order_id, items=items)

    def _initialize_schema(self) -> None:
        self._database_path.parent.mkdir(parents=True, exist_ok=True)
        with closing(sqlite3.connect(self._database_path)) as connection:
            with connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS orders (
                        order_id TEXT PRIMARY KEY,
                        items_json TEXT NOT NULL,
                        subtotal REAL NOT NULL,
                        discount REAL NOT NULL,
                        final_amount REAL NOT NULL
                    )
                    """
                )

