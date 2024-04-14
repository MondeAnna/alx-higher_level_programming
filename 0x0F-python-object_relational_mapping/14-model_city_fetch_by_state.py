#!/usr/bin/python3


"""
Fetch Cities by State
"""


import sys
import sqlalchemy as sa
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State


def main(user, password, database):
    engine = sa.create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, database
        ),
        pool_pre_ping=True,
    )

    with Session(bind=engine) as session:
        query = session.query(
            State.name,
            City.id,
            City.name,
        ).join(
            State
        ).all()

    for row in query:
        print("{}: ({}) {}".format(
            row[0], row[1], row[2],
        ))


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
