def process_payment(order_id: str, amount: float) -> bool:
    if not order_id.strip():
        raise ValueError("Order id must not be empty.")
    if amount <= 0:
        raise ValueError("Payment amount must be positive.")
    return True

