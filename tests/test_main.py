import pytest

from src.main import calculate_total, calculate_average


def test_calculate_total():
    assert calculate_total(100, 5) == 500


def test_zero_quantity():
    assert calculate_total(100, 0) == 0


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total(-10, 2)


def test_empty_average():
    with pytest.raises(ValueError):
        calculate_average([])