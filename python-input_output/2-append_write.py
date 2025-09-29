#!/usr/bin/python3
"""
File for appending text in a file
"""


def append_write(filename="", text=""):
    """Function to append a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
