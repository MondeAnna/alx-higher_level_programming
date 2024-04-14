#!/usr/bin/python3

"""
Create City Model
"""


import sqlalchemy as sa
from sqlalchemy.orm import relationship
from model_state import Base


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
