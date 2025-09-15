#!/usr/bin/python3
"""Rectangle class file

contains an empty recangle class
"""


class Rectangle:
    """Rectangle class to do basic rectangle operations

    Attributes:
        number_of_instances(int): stores the number of instances of rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1
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

    def __str__(self):
        """special method that returns a string

        Returns:
            empty string if width or height is equal to 0
            else a string formated like the print function
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        toprint = ""
        for i in range(self.__height):
            for _ in range(self.__width):
                toprint += str(self.print_symbol)
            toprint += "\n" if i < self.__height - 1 else ""

        return toprint

    def __repr__(self):
        """special method that returns a dev friendly string

        Returns:
            a formated string for developpers
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """special method that prints a message when deleting a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __new__(cls, width=0, height=0):
        """special method that triggers whenver a new object is created"""
        instance = super(Rectangle, cls).__new__(cls)
        return instance

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """a static method for comparing 2 rectangle area

        compare 2 reactangle area

        Args:
            rect_1(obj): a Rectangle
            rect_2(obj): a Rectangle

        Returns:
            rect_1 if rect_1 is >= rect_2
            otherwise rect_2
        Raise:
            TypeError: if rect_1 or rect_2 are not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """a class method that creates a new square rectangle

        Args:
            size(int): represent a square size
        Returns:
            a new rectangle with square dimension
        """
        return cls(size, size)
