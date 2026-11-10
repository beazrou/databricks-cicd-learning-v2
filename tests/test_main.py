import pytest

from src.main import calculate_total, calculate_average, calculate_discount


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



def test_calculate_discount():
    assert calculate_discount(100, 20) == 80


def test_no_discount():
    assert calculate_discount(100, 0) == 100


def test_full_discount():
    assert calculate_discount(100, 100) == 0


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 120)
