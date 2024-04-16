#!/usr/bin/python3
"""no moduel"""


def inherits_from(obj, a_class):
    """
    checjing the type
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
