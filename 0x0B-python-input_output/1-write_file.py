#!/usr/bin/python3
"""Defines a file-writing function"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
