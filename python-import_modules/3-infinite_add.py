#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = 0
    for i in range(1, len(argv)):
        n += int(argv[i])
    print("{:d}".format(n))
