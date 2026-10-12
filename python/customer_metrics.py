def average_spend(total_spend, number_of_orders):
    """Return average spending per order, including the zero-order case."""
    if number_of_orders == 0:
        return 0.0
    return total_spend / number_of_orders
