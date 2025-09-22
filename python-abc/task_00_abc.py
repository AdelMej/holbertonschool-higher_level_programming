"""
a file containing the class of animals
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    an abstract class for animals
    """

    @abstractmethod
    def sound(self) -> str:
        """ abstract method for animal sound """
        pass


class Dog(Animal):
    """
    a dog class inheriting from animal
    """

    def sound(self):
        """ the sound a dog makes """
        return "Bark"


class Cat(Animal):
    """
    a cat class inheriting from animal
    """

    def sound(self):
        """ the sound of a cat"""
        return "Meow"
