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
