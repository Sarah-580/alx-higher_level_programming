#!/usr/bin/python3
"""Class Square is defined"""


class Square:
    """Class Square is Represented"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize Class Square

        size: size of new square
        """
    self.size = size
    self.position = position

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

    @property
    def position(self):
        """set position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
                for _ in range(self.__position):
                    print(" " * self.__position[0] + "#" * self.__size)
