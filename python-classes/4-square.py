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

    def area(self):
        """area method

        Returns:
            area of the square
        """
        return (self.__size**2)

    @property
    def size(self):
        """property function
        Returns:
            __size(int): private size Attribute
        """
        return self.__size

    @size.setter
    def size(self, size):
        """size setter function

        set the private size to a given value
        Raises:
            TypeError: if size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        self.__size = size

    @size.getter
    def size(self):
        """size getter function

        function to get size

        Returns:
            __size(int): the private size attribute
        """
        return self.__size
