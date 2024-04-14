#!/usr/bin/python3


"""
Safely filtered user query
"""

import MySQLdb as db
import sys


def main(user, password, database, state):
    connection = db.connect(
        user=user,
        password=password,
        database=database,
        host="localhost",
        port=3306,
    )

    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE %s""", [state])

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


if __name__ == "__main__":
    *_, user, password, database, state = sys.argv
    main(user, password, database, state)
