#!/usr/bin/python3


"""
Join `cities` and `states` tables
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
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
          FROM cities
          JOIN states
         WHERE cities.state_id = states.id
         ORDER BY cities.id;
    """)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
