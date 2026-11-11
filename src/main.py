
def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be positive")

    return price * quantity


def calculate_average(values):
    if not values:
        raise ValueError("The list cannot be empty")

    return sum(values) / len(values)


def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    discount = price * discount_percent / 100
    return price - discount


def calculate_order_total(price, quantity, discount_percent):
    total = calculate_total(price, quantity)
    return calculate_discount(total, discount_percent)
