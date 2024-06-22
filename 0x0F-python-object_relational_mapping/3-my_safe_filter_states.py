#!/usr/bin/python3
"""write a script that takes in arguments and displays all values"""
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    argv = sys.argv
    db = mysql.connect(host="localhost", port=3306, user=argv[1],
                       password=argv[2],
                       database=argv[3])
    c = db.cursor()
    qury = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    c.execute(qury, (argv[4],))
    rows = c.fetchall()
    for row in rows:
        print(row)
