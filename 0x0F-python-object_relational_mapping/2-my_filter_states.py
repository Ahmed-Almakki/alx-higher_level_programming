#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values"""
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    argv = sys.argv
    db = mysql.connect(host="localhost", port=3306, 
                       user=argv[1],
                       password=argv[2],
                       database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                   FROM states \
                   WHERE BINARY `name` = '{}' \
                   ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
