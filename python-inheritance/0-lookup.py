#!/usr/bin/python3
"""a file containing a function for looking up object methods and attributes
"""


def lookup(obj):
    """function to lookup object methods and attributes,
    attributes of a class return a list

    Args:
        obj(obj): an objeect to look at it's methods
    Return:
        a list of the object methods and attributes
    """
    return dir(obj)
