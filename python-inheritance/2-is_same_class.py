#!/usr/bin/python3

"""
a file containing a functioin that return if an object is from a class
"""


def is_same_class(obj, a_class):
    """a function that return if an obj is an instance of a class"""
    return type(obj) is a_class
