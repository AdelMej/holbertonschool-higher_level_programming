#!/usr/bin/python3

""" a file containing a function that returns if
an object is a sublclass of a class return false otherwise
"""


def inherits_from(obj, a_class):
    """ a function that returns if an obj
    is an instance of a class that ineherited from a specific class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
