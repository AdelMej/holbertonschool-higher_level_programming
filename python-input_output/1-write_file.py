#!/usr/bin/python3
"""
File for writing text in a file
"""


def write_file(filename="", text=""):
    """Function to write in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
