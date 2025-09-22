#!/usr/bin/python3

""" a file containing a function that returns if
an object is a sublclass of a class return false otherwise
"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) is not a_class
