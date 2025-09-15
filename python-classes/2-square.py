#!/usr/bin/python3
"""square class file

empty class for now
"""


class Square():
    """square class for square operations

    does nothing

    Attributes:
        no Attributes
    """
    def __init__(self, size=0):
        """Square constructor

        Attributes:
            size(int): the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
