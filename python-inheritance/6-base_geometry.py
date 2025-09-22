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
