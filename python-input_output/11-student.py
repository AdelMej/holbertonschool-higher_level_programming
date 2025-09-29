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
            for i in attrs:
                if i in self.__dict__:
                    result[i] = self.__dict__[i]
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Function to relaod my class from a json"""
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
