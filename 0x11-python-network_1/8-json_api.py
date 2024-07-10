#!/usr/bin/python3
""" script that takes in a letter and sends a POST"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    parm = {'q': q}
    x = requests.post("http://0.0.0.0:5000/search_user", data=parm) 
    js = x.json()
    if js == {}:
        print("No result")
    else:
        print("[{}] {}".format(js.get("id"), js.get("name")))
