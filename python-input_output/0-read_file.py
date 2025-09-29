#!/usr/bin/python3
"""
file containing code to read a file
"""


def read_file(filename=""):
    """Function to read a file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
