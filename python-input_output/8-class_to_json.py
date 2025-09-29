#!/usr/bin/python3
"""
File to store an object in json format
"""


def class_to_json(obj):
    """Function to store a class in a json file"""
    return obj.__dict__
