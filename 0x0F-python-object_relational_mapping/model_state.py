#!/usr/bin/python3

"""
Create State Model
"""


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    name = sa.Column("name", sa.String(128), nullable=False)
    id = sa.Column(
        "id",
        sa.Integer,
        nullable=False,
        primary_key=True,
    )
