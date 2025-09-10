#!/usr/bin/python3
"""A library containing a say my name function

say my name is function that prints a given name
it should be type safe
"""


def say_my_name(first_name, last_name=""):
    """print a full name

    Args:
        first_name(str): the first name
        last_name(str): the last name
    Returns:
        None
    Raises:
        TypeError: first_name should be a string
        TypeError: last_name should be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
