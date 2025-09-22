#!/usr/bin/python3
"""
a file containing a class that inherit list
has a custom print function
"""


class MyList(list):
    """ a simple list class
    that has a custom print function
    """

    def print_sorted(self):
        """ function that prints a sorted version of the list"""
        copy = self.copy()
        copy.sort()
        print(copy)
