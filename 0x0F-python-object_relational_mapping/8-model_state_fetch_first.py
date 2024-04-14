#!/usr/bin/python3


"""
Prints first `State` in database
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
    state = session.query(State).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
