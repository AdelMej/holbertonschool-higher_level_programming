#!/usr/bin/python3
"""
a file containing the class geometry
"""


class BaseGeometry:
    """ a class for basic geometry"""

    def area(self):
        """ a function to calculate the area of a geometry

        Raises:
            Exception: if the area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validate an integer
        Args:
            name(str): the name of the value
            value(int): the value to test
        Raise:
            TypeError if value is not an integer
            ValueError if value is lower or equal than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
