#!/usr/bin/python3
"""no moduel"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written
    """
    i = 0
    with open(filename, "w", encoding="utf-8") as f:
        i = f.write(text)
    return i
