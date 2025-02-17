from calc import sum
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),    # Test with two positive numbers
    (-1, -1, -2), # Test with two negative numbers
    (0, 0, 0),    # Test with zero values
    (10, -5, 5),  # Test with mixed positive and negative numbers
    (100, 200, 300), # Test with larger numbers
])
def test_sum_positive(a, b, expected):
    assert sum(a, b) == expected

def test_sum_negative():
    assert sum(-1, -1) == -2

def test_sum_zero():
    assert sum(0, 0) == 0

