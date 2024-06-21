#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    db = mysql.connect(host="localhost", user=sys.argv[1],
                       password=sys.argv[2], database=sys.argv[3], port=3306)

cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
