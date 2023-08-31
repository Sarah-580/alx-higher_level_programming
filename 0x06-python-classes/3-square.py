#!/usr/bin/python3
"""Class Square is defined"""


class Square:
    """Class Square is Represented"""

    def __init__(self, size=0):
        """
        Initialize Class Square

        size: size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of Square"""
        return (self.__size * self.__size)
