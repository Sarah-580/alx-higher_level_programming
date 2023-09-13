#!/usr/bin/python3
"""Module inherits from list class"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """prints a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
