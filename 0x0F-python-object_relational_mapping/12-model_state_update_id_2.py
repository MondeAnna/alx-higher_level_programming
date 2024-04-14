#!/usr/bin/python3


"""
Update State
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

    with Session(bind=engine) as session:
        session.query(State).filter(State.id.like(2)).update(
            {"name": "New Mexico"},
            synchronize_session="fetch",
        )
        session.commit()


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
