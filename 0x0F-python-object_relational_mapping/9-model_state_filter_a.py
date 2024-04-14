#!/usr/bin/python3


"""
Filter State Model Objects
"""


import sys
import sqlalchemy as sa
from sqlalchemy.orm import Session
from model_state import Base, State


def main(user, password, database):
    engine = sa.create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, database
        ),
        pool_pre_ping=True,
    )

    session = Session(bind=engine)
    states = session.query(State).filter(State.name.like("%a%"))

    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
