#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""
import sys
import requests


if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    status = x.status_code
    if status < 400:
        print("Index")
    else:
        print("Error code: {}".format(status))
