"""
This code defines four basic arithmetic functions:
-add(a, b): it takes two numbers, a and b, as input and returns their sum.
-subtract(a, b): it takes two numbers, a and b, as input and returns their difference (a - b).
-multiply(a, b): it takes two numbers, a and b, as input and returns their product.
-divide(a, b): ittakes two numbers, a and b, as input and returns their quotient (a / b).
It also includes a check for division by zero. If b is zero, it raises a ValueError to prevent a ZeroDivisionError.
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(a):
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result # expected result

def power(a, b):
    return a ** b

def prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

def input_number():
    entry = input("Enter one or two numbers separated by a space:")
    if len(entry.split()) == 1:
        return int(entry)
    else:
        return list(map(int, entry.split()))

