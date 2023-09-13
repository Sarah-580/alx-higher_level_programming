#!/usr/bin/python3
"""Module defines a Rectangle subclass Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a anew square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size