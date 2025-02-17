from calc import sum

def test_sum_positive():
    assert sum(2, 3) == 5

def test_sum_negative():
    assert sum(-1, -1) == -2

def test_sum_zero():
    assert sum(0, 0) == 0