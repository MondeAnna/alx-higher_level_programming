#!/usr/bin/python3


"""
Filter State Model Objects with User Arg
"""


import sys
import sqlalchemy as sa
from sqlalchemy.orm import Session
from model_state import Base, State


def main(user, password, database, state):
    engine = sa.create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, database
        ),
        pool_pre_ping=True,
    )

    session = Session(bind=engine)
    states = session.query(State).filter(State.name.like(state)).all()

    if not states:
        print("Not found")
    else:
        for state in states:
            print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    *_, user, password, database, state = sys.argv
    main(user, password, database, state)
