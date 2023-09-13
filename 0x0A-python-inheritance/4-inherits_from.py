#!/usr/bin/python3
"""
checks if object is an instance of an class that inherited
from the specified class or not
"""



def inherits_from(obj, a_class):
    """
     Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
