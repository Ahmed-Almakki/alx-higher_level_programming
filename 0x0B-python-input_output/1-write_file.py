#!/usr/bin/python3
"""no moduel"""


def write_file(filename="", text=""):
    """writes a string to a text file returns the number of characters
    """
    i = 0
    with open(filename, "w", encoding="utf-8") as f:
        i = f.write(text)
    return i
