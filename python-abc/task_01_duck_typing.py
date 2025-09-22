"""
file containing shape classes
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ abstract class defining a shape """
    @abstractmethod
    def area(self):
        """ abstract method for the area of a shape """
        pass

    @abstractmethod
    def perimeter(self):
        """ abstract method for the perimeter of a shape"""
        pass


class Circle(Shape):
    """ a class representing a circle """
    def __init__(self, radius):
        """ Circle constructor """
        self.radius = radius

    def area(self):  # type:ignore
        """ a method that return the area of a circle"""
        return pi * self.radius**2

    def perimeter(self):  # type: ignore
        """ a method that return the perimeter of a circle """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """ a class representing a rectangle """
    def __init__(self, width, height) -> None:
        """ Rectangle constructor """
        self.width = width
        self.height = height

    def area(self):  # type: ignore
        """ a method returning the area of a rectangle """
        return self.width * self.height

    def perimeter(self):  # type: ignore
        """ a method returning the perimeter of a rectangle """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ a function that print shape information """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
