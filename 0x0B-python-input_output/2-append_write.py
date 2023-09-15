#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    Returns the number of characters added
    """
    with open(filename, "a", encoding='utf=8') as a_file:
        return a_file.write(text)
