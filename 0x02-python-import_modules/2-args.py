#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ln = len(argv)
    if ln - 1 == 0:
        print("0 arguments.")
    if ln - 1 == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    if ln - 1 > 1:
        print("{} arguments:".format(ln - 1))
        for i in range(1, ln):
            print("{}: {}".format(i, argv[i]))
