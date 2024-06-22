#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    argv = sys.argv
    db = mysql.connect(host="localhost", port=3306,
                       user=argv[1],
                       password=argv[2],
                       database=argv[3])
    c = db.cursor()
    qury = "SELECT cities.id, states.name, cities.name \
            FROM cities INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
    c.execute(qury)
    rows = c.fetchall()
    for row in rows:
        print(row)
