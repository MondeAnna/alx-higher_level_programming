#!/usr/bin/python3


"""
Insert Relational State Object
"""


import sys
import sqlalchemy as sa
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import Base, City


def main(user, password, database):
    engine = sa.create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, database
        ),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)

    city = City(name="San Francisco")

    state = State(name="California")
    state.cities.append(city)

    with Session(bind=engine) as session:
        session.add_all([city, state])
        session.commit()


if __name__ == "__main__":
    *_, user, password, database = sys.argv
    main(user, password, database)
