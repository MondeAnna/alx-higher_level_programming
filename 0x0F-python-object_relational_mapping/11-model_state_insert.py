#!/usr/bin/python3


"""
Insert State
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

    state = State(name="Louisiana")

    with Session(bind=engine) as session:
        session.add(state)
        session.commit()
        session.refresh(state)

    print(state.id)


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
