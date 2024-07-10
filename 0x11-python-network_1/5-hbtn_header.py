#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays"""
import requests
import sys


if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    print(x.headers["X-Request-Id"])
