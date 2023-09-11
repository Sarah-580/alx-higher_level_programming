#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    adds 2 integers.

    Args:
    a (int or float): first integer or float
    b (int or float, default 98): second integer or float

    Returns:
    int: the addition of a and b, casted to an integer

    Raises:
    TypeError: If a or b is not an integer or a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
