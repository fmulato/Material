"""
This file contains unit tests for verifying the functionality of a simple calculator module
using the pytest framework in Python.

The tests cover basic arithmetic operations: addition, subtraction, multiplication, and division,
ensuring that each function behaves as expected.

The file starts by importing the necessary functions from the calculator module and the pytest library.

Each arithmetic operation is tested in a separate function.

Overall, these tests ensure that the calculator functions perform as expected and handle edge cases appropriately.

'assert' is a reserved word in Python, that is used to check if a condition is true or false.

"""
import pytest
from calculator import add, subtract, multiply, divide, factorial, power, prime

def test_add():
    assert add(2, 3) == 5 # expected result

def test_subtract():
    assert subtract(10, 5) == 5  # expected result

def test_multiply():
    assert multiply(3, 4) == 12  # expected result

def test_divide():
    assert divide(10, 2) == 5  # expected result

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)  # expected result

def test_factorial():
    assert factorial(5) == 120 # expected result

def test_power():
    assert power(5, 2) == 25 # expected result

def test_factorial():
    assert factorial(5) == 120

def test_power():
    assert power(5, 2) == 25

def test_prime():
    assert prime(11)
    assert not prime(10)

