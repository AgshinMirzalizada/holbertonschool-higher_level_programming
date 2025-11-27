#!/usr/bin/python3
"""Module that define a function to check if an object inherits from a class"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
