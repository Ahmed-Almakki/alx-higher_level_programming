#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    ln = len(argv) - 1
    res = 0
    if ln == 0:
        print("0")
    else:
        for i in range (1, ln + 1):
            res = int(argv[i]) + res
        print(res)
