import math


def factorial(n):
    """Calculates the factorial of a number.

    Args:
        n (int): Number to calculate factorial of.

    Raises:
        ValueError: n must be >= 0
        ValueError: n must be an exact integer
        OverflowError: n is too large

    Returns:
        int: Result of factorial calculation.

    >>> factorial(-1)
    Traceback (most recent call last):
    ValueError: n must be >= 0
    >>> factorial(1.5)
    Traceback (most recent call last):
    ValueError: n must be exact integer
    >>> factorial(1e300)
    Traceback (most recent call last):
    OverflowError: n too large
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(10)
    3628800
    """
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")

    result = 1
    factor = 2

    while factor <= n:
        result *= factor
        factor += 1

    return result
