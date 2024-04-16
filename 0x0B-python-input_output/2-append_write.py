#!/usr/bin/python3
"""no moduel"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    """
    i = 0
    with open(filename, "a", encoding="utf-8") as f:
        i = f.write(text)
    return i
