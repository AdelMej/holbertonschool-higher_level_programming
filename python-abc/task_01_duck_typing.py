#!/usr/bin/python3
"""File containing shape classes"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class defining a shape"""
    @abstractmethod
    def area(self):
        """Abstract method for the area of a shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for the perimeter of a shape"""
        pass


class Circle(Shape):
    """Class representing a circle"""
    def __init__(self, radius):
        """Circle constructor"""
        self.radius = radius

    def area(self):  # type:ignore
        """Method that return the area of a circle"""
        return math.fabs(math.pi * (self.radius**2))

    def perimeter(self):  # type: ignore
        """Method that return the perimeter of a circle """
        return math.fabs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """Class representing a rectangle"""
    def __init__(self, width, height):
        """Rectangle constructor """
        self.width = width
        self.height = height

    def area(self):  # type: ignore
        """Method returning the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):  # type: ignore
        """Method returning the perimeter of a rectangle"""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Function that print shape information"""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
