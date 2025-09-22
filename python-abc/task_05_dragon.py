#!/usr/bin/python3
"""
File containing a dragon
"""


class SwimMixin:
    """SwimMixin class"""
    def swim(self):
        """swim method"""
        print("The creature swims!")


class FlyMixin:
    """FlyMixin class"""
    def fly(self):
        """fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""
    def roar(self):
        """Roar method"""
        print("The dragon roars!")
