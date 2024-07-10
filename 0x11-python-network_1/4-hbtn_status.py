#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    x = requests.get("https://alx-intranet.hbtn.io/status")
    i = [ii.decode('utf-8') for ii in x]
    print("Body response:\n\
                - type: {}\n\
                - content: {}".format(type(i[0]), i[0]))
