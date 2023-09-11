#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix

    Args:
        matrix (list): A list of lists of ints or floats
        div (int/float): The divisor

    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0

    Returns:
        A new matrix representing the result of the division
    """

    if not matrix:
        raise TypeError(errorMessage)
    if not isinstance(matrix, list):
        raise TypeError(errorMessage)

    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)

    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(errorMessage)
        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")
        if not all(len(lists) == len(matrix[0]) for lists in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        return [[round(item / div, 2) for item in lists] for lists in matrix]
