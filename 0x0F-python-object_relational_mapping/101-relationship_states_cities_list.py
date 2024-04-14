#!/usr/bin/python3


"""
Fetch Cities by State
"""


import sys
import sqlalchemy as sa
from sqlalchemy.orm import Session
from relationship_state import State


def main(user, password, database):
    engine = sa.create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, database
        ),
        pool_pre_ping=True,
    )

    with Session(bind=engine) as session:
        states = session.query(State)

    for state in states:
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("{}: {}".format(city.id, city.name))


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
