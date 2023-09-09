#!/usr/bin/python3
"""define Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """init for Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """return representation of the Rectangle"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
