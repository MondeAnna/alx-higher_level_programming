#!/usr/bin/python3


"""
Query `cities` in user provided `state`
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

    cursor.execute(
        """
            SELECT cities.id, cities.name
              FROM cities
              JOIN states
             WHERE cities.state_id = (
                   SELECT states.id
                     FROM states
                    WHERE states.name = %s)
             ORDER BY cities.id;
        """,
        [state]
    )

    cities = {row for row in cursor.fetchall()}

    sorted_cities = [
        city
        for _, city
        in sorted(cities, key=lambda x: x[0])
    ]

    print(", ".join(sorted_cities))

    connection.close()


if __name__ == "__main__":
    *_, user, password, database, state = sys.argv
    main(user, password, database, state)
