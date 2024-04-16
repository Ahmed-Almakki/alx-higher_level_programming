#!/usr/bin/python3
"""no moduel"""


def read_file(filename=""):
    """readfile reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
