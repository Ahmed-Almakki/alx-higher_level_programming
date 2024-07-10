#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST"""
import sys
import requests


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    value = {'email': email}
    x = requests.post(url, data=value)
    print(x.text)
