#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("{} argument".format(len(sys.argv) - 1), end="s:\n" if len(sys.argv) > 2 else "\n" if len(sys.argv) == 2 else "s.\n")
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
