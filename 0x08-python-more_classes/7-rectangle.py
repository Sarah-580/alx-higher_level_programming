#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """
    Rectangle class representation

    Attributes:
        number_of_instances (int): The number of Rectangle instances
        print_symbol (any): The symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """get/set width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return presentation of the Rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
            for _ in range(self.__height)])

    def __repr__(self):
        """Return printable presentation of the Rectangle"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Prints a message for every deletion of a Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
