#!/usr/bin/python3
"""
File to serialize input in json string
"""
import json


def from_json_string(my_obj):
    """Function to convert an object into json string"""
    return json.loads(my_obj)
