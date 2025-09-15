#!/usr/bin/python3
"""Rectangle class file

contains an empty recangle class
"""


class Rectangle:
    """Rectangle class to do basic rectangle operations

        does nothing
    """
    def __init__(self, width=0, height=0):
        """recangle constructor

        Args:
            width(int): the rectangle width
            height(int): the recangle height
        Raises:
            TypeError: if width or height are not int
            ValueError: if width or height are < 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width property method
        creates a property for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter function
            function that allows quick setting for width

        Args:
            value(int): the new height value
        Raise:
            TypeError: if value is not an int
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height property method
        created a property for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter function
            function that allows quick setting for height

        Args:
            value(int): the new height value
        Raise:
            TypeError: if value is not an int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """method that returns the area of the rectangle

        Returns:
            the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """method that returns the perimeter of the rectangle

        Returns:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2
