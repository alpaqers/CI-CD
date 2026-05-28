"""Calculator application functions"""


def add(a: int, b: int) -> int:
    """Return sum of two numbers"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return difference of two numbers"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return product of two numbers"""
    return a * b


def divide(a: int, b: int) -> float:
    """Return quotient of two numbers"""
    return a / b


def decimal_to_binary(n: int) -> str:
    """Convert a decimal number to binary string"""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0 or n > 100:
        raise ValueError("Number must be in range from 0 to 100")

    if n == 0:
        return "0"
    return bin(n)[2:]
