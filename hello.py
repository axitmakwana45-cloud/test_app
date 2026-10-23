"""Basic math utilities for a simple test repository."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    c = a+b
    return c
    


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    c = a - b
    if(c > 0):
        return c
    return 0

    if(c > 0):
            return c
    return 0

def hello(name : str) -> str:
    return f"hello {name}"

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def average(numbers: list[float]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(numbers) / len(numbers)


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def is_prime(n: int) -> bool:
    """Return True when n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n ** 0.5) + 1
    for value in range(3, limit, 2):
        if n % value == 0:
            return False
    return True


def main() -> None:
    """Run a quick demonstration of the math helpers."""
    numbers = [2, 4, 6, 8]
    print(f"Add: {add(10, 5)}")
    print(f"Subtract: {subtract(10, 5)}")
    print(f"Multiply: {multiply(10, 5)}")
    print(f"Divide: {divide(10, 5)}")
    print(f"Average: {average(numbers)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Is 17 prime? {is_prime(17)}")


if __name__ == "__main__":
    main()
