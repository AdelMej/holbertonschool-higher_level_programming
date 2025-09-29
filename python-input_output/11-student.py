#!/usr/bin/python3
"""
File that contains a student class
"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Student constructor"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """Json represnetation of the student class"""
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if isinstance(attr, str) and attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Function to relaod my class from a json"""
        for key in json:
            if key in self.__dict__:
                setattr(self, key, json[key])
