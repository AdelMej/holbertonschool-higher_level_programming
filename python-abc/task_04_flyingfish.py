#!/usr/bin/python3
"""
a file containing a flying fish beware
"""


class Fish:
    """Class fish"""
    def swim(self):
        """Swim printing method"""
        print("The fish is swimming")

    def habitat(self):
        """Habitat printing method"""
        print("The fish lives in water")


class Bird:
    """Class bird"""
    def fly(self):
        """flying printing method"""
        print("The bird is flying")

    def habitat(self):
        """habitat printing method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class FlyingFish"""
    def fly(self):
        """Flying printing method"""
        print("The flying fish is soaring!")

    def swim(self):
        """Swim printing method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Habitat printing method"""
        print("The flying fish lives both in water and the sky!")
