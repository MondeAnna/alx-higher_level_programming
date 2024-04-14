#!/usr/bin/python3


"""
Create Relationship with City
"""


from sqlalchemy.orm import relationship
import sqlalchemy as sa
from relationship_city import Base, City


class State(Base):
    __tablename__ = "states"

    name = sa.Column("name", sa.String(128), nullable=False)

    id = sa.Column(
        "id",
        sa.Integer,
        nullable=False,
        primary_key=True,
    )

    cities = relationship(City, backref="state", cascade="all, delete")
