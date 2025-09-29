#!/usr/bin/python3
"""
File containing a function to save obj in json files
"""
import json


def save_to_json_file(my_obj, filename):
    """Function to save a file in json format"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
