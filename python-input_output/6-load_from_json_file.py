#!/usr/bin/python3
"""
File that loads an object from a json file
"""
import json


def load_from_json_file(filename):
    """Function that loads an object from a json file"""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
