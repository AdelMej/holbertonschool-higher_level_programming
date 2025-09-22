#!/usr/bin/python3
"""
a file containing the class square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class for squares """
    def __init__(self, size):
        """
        square constructor
        Args:
            size(int): the square size
        """
        self.__size = size
        super().__init__(self.__size, self.__size)
