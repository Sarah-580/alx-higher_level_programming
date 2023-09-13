#!/usr/bin/python3
"""Defines a class Rectangle that inherites from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a anew Rectangle"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        seif.integer_validator("height", height)

        def area(self):
            """returns the area of the Rectangle"""
            return self.__width * self.__height

        def __str__(self):
            """returns the print() and str() representation of the Rectangle"""
            return str("[Rectangle] {}/{}".format(self.__width, self.__height))
