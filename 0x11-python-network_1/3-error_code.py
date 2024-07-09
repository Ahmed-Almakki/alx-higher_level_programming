#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays"""
import sys
import urllib
import urllib.request as req


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with req.urlopen(url) as resp:
            print("Index")
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
