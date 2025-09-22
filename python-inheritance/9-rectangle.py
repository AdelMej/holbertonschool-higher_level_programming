#!/usr/bin/python3
"""
a file containing the class rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class for rectangles """

    def __init__(self, width, height):
        """ rectangle constructor

        Args:
            width(int): an integer representing the rectangle width
            height(int): an integer representing the rectangle height

        Raises:
            TypeError: width or height are not integers
            ValueError: if width or height are <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ implementation of the area for rectangles

        Returns:
            the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        function for printing
        format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
