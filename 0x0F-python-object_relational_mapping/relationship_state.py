#!/usr/bin/python3

"""Contains class definition of a State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Class defining the states table. Inherits from Base."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        order_by="asc(City.id)",
        cascade="all, delete",
        passive_deletes=True,
        backref="state",
    )
