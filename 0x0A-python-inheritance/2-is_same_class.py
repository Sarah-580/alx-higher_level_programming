#!/usr/bin/python3
"""Checks if object is an instance of a class"""



def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is an instance of a_class, False otherwise
    """

    return True if type(obj) is a_class else False
