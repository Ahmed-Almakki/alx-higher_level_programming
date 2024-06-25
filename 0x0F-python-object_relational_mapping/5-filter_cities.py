#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument"""
import MySQLdb as mysql
import sys


if __name__ == "__main__":
    argv = sys.argv
    db = mysql.connect(host="localhost", port=3306,
                       user=argv[1],
                       password=argv[2],
                       database=argv[3])
    c = db.cursor()
    qury = "SELECT cities.name \
            FROM cities INNER JOIN states \
            ON states.id = cities.state_id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC"
    r = c.execute(qury, (argv[4],))
    rows = c.fetchall()
    i = 1 
    if (len(argv) == 5 and r != 0):
        for row in rows:
            print(row[0], end="")
            if i != len(rows):
                print(",", end=" ")
            else:
                print()
            i += 1
    else:
        print()
