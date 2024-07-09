#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import sys
from urllib.request import urlopen


with urlopen(sys.argv[1]) as response:
    res = response.info()
    x = res.get("X-Request-Id")

print(x)
