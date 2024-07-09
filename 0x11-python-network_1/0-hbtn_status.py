#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/stat"""
import urllib
from urllib.request import urlopen


with urlopen("https://alx-intranet.hbtn.io/status") as response:
    res = response.read()
    head = response.info()
    content = head.get('Content-Type')

if content.split("=")[1] == 'utf-8':
    ok = "OK"
print("Body response:\n\
    - type: {}\n\
    - content: {}\n\
    - utf8 content: {}".format(type(res), res, ok))
