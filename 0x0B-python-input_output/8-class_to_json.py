#!/usr/bin/python3
"""json moduel"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    """
    return json.dumps(obj, default=lambda obj: obj.__dict__)
