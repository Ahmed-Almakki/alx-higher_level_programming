#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request"""
import urllib.request as req
import urllib.parse as parse
import sys


if __name__ == "__main__":
    argv = sys.argv
    email = str(argv[2])
    url = argv[1]
    value = {'email': email}
    email = parse.urlencode(value)
    email = email.encode('ascii')
    rq = req.Request(url, email)
    with req.urlopen(rq) as resp:
        rs = resp.read()
    print(rs.decode('utf-8'))
