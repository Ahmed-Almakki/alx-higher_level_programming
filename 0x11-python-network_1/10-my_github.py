#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)"""
import sys
import requests


if __name__ == "__main__":
    name = sys.argv[1]
    passw = sys.argv[2]
    parm = requests.auth.HTTPBasicAuth(name, passw)
    x = requests.get("https://api.github.com/user", auth=parm)
    print(x.json().get("id"))
