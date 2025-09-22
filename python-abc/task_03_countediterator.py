#!/usr/bin/python3
"""
File containing a class for a Counted Iterator
"""


class CountedIterator:
    """
    Class extending iterator behavior
    """
    def __init__(self, obj):
        """CountedIterator constructor"""
        self.__counter = 0
        self.__iterator = iter(obj)

    def get_count(self):
        """return current iteration"""
        return self.__counter

    def __next__(self):
        """rewrite next to increment counter"""
        res = next(self.__iterator)
        self.__counter += 1
        return res
