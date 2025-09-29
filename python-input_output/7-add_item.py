#!/usr/bin/python3
"""
File to save and load from add_item.json
"""
from sys import argv
import os.path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    """Main"""
    if os.path.exists("add_item.json"):
        res = load_from_json_file("add_item.json")
    else:
        res = []

    res.extend(argv[1:])
    save_to_json_file(res, "add_item.json")
