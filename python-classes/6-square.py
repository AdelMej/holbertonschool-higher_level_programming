#!/usr/bin/python3
"""square class file

empty class for now
"""


class Square():
    """square class for square operations

    store meta data for squares
    """

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor

        Args:
            size(int): the size of the square
            position(tuple): the position of the square

        Raises:
            TypeError: if size is not an integer
            TypeError: if position is not a tuple
            TypeError: if position is not a tuple of int
            TypeError: if position int are < 0
            ValueError: if size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or all(isinstance(i, int) and i < 0 for i in position)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__size = size
        self.__position = position

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
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @size.getter
    def size(self):
        """size getter function

        function to get size

        Returns:
            __size(int): the private size attribute
        """
        return self.__size

    @property
    def position(self):
        """property function

        Returns:
            __position(tuple): private position value
        """
        return self.__position

    @position.setter
    def position(self, position):
        """position setter function

        Raises:
            TypeError: if position is not a tuple
            TypeError: if position isn't a int tuple
            TypeError: if position tuple ints are negative
        """
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or all(isinstance(i, int) and i <= 0 for i in position)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = position

    @position.getter
    def position(self):
        """ position function getter

        Returns:
            __position(tuple): private attribute position
        """
        return self.__position

    def my_print(self):
        """print a square

        function that print a square
        """
        if (self.__size == 0):
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(end=" ")

            for _ in range(self.__size):
                print("#", end="")
            print()


