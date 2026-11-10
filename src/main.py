def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be positive")

    return price * quantity


def calculate_average(values):
    if not values:
        raise ValueError("The list cannot be empty")

    return sum(values) / len(values)