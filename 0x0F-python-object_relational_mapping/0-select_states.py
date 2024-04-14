#!/usr/bin/python3


"""
Select all entries in the `States` table of the user provided database
"""

import MySQLdb as db
import sys


def main(user, password, database):
    connection = db.connect(
        user=user,
        password=password,
        database=database,
        host="localhost",
        port=3306,
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
