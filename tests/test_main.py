
import pytest

from src.main import (
    calculate_total,
    calculate_average,
    calculate_discount,
    calculate_order_total,
)


def test_calculate_total():
    assert calculate_total(10, 3) == 30


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total(-10, 3)


def test_empty_average():
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_discount():
    assert calculate_discount(100, 20) == 80


def test_full_discount():
    assert calculate_discount(100, 100) == 0


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 120)


def test_calculate_order_total():
    assert calculate_order_total(100, 3, 20) == 240


def test_order_without_discount():
    assert calculate_order_total(100, 2, 0) == 200


def test_order_with_zero_quantity():
    assert calculate_order_total(100, 0, 20) == 0
