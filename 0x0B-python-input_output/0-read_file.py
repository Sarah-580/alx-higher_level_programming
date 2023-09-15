#!/usr/bin/python3
"""Define a text file-reading function"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout"""
    with open(filename, 'r') as f:
        for li in f:
            print(li, end="")
            f.closed
