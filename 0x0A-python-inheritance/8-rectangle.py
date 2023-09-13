#!/usr/bin/python3
"""inherit from BaseGeometry"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize new Rctangle"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
