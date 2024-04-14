#!/usr/bin/python3

"""
Create Relations with State
"""


import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base


Base = declarative_base()


class City(Base):
    __tablename__ = "cities"

    name = sa.Column("name", sa.String(128), nullable=False)

    state_id = sa.Column(
        "state_id",
        sa.Integer,
        sa.ForeignKey("states.id"),
        nullable=False,
    )

    id = sa.Column(
        "id",
        sa.Integer,
        nullable=False,
        primary_key=True,
    )
