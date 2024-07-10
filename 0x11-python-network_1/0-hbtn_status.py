#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/stat"""
import urllib
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        res = response.read()

    print("Body response:\n\
    - type: {}\n\
    - content: {}\n\
    - utf8 content: {}".format(type(res), res, res.decode(encoding='utf-8')))
