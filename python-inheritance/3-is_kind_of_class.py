#!/usr/bin/python3
"""
a file containing a function that returns
if an object is a kind of class
"""


def is_kind_of_class(obj, a_class):
    """ returns if the obj is a subclass of a_class"""
    return isinstance(obj, a_class)
