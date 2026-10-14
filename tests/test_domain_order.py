import unittest

from src.domain.models import Order, OrderItem


class TestOrderDomain(unittest.TestCase):
    def test_order_discount_applied(self) -> None:
        items = [
            OrderItem("1", "Server Rack", 4000.0, 1),
            OrderItem("2", "Patch Cord", 1500.0, 1),
        ]

        order = Order("ORD-001", items)

        self.assertEqual(order.calculate_subtotal(), 5500.0)
        self.assertEqual(order.calculate_discount(), 550.0)
        self.assertEqual(order.calculate_final_amount(), 4950.0)

    def test_order_without_discount(self) -> None:
        order = Order("ORD-002", [OrderItem("3", "Switch", 2000.0, 1)])

        self.assertEqual(order.calculate_final_amount(), 2000.0)

    def test_empty_order_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Order("ORD-003", [])

    def test_invalid_quantity_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            OrderItem("4", "Cable", 100.0, 0)


if __name__ == "__main__":
    unittest.main()

