#!/usr/bin/python3
"""add function utility.

Provides an utility function for adding numbers
Accept floats and integer values
"""


def add_integer(a, b=98):
    """add 2 integers together.

    Args:
        a (int, float): a value to add to b
        b (int, float): a value to add to a

    Returns:
        int: The result of a + b

    Raises:
        TypeError: if a or b is not a float or an integer

    Example:
        >>> add_integer(2, 2)
        4
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
