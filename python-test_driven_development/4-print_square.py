#!/usr/bin/python3
#!/usr/bin/python3-config
"""a library to print a square

can print a square depending on a given integer
should be type safe guarded
"""


def print_square(size):
    """Prints a square.
    
    Args:
        size(int): the size of the square

    Returns:
        None

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
