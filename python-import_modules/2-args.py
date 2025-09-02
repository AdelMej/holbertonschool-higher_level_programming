#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = len(argv) - 1
    end_char = "s:" if n > 1 else ":" if n == 1 else "s."
    print("{} argument{}".format(n, end_char))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
