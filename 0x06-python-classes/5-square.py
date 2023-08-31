#!/usr/bin/python3
"""Class Square is defined"""


class Square:
    """Class Square is Represented"""

    def __init__(self, size=0):
        """
        Initialize Class Square

        size: size of new square
        """
        self.size = size

    @property
    def size(self):
        """set size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
