#!/usr/bin/python3
"""Module defines a Rectangle subclass Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a anew square"""
        super().__init__(size, size)

        def __str__(self):
            """return strig representation"""
            return "[Square] {}/{}".format(self._Rectangle__width,
                    self._Rectangle__height)
