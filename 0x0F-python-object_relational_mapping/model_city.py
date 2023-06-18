#!/usr/bin/python3

"""Implementation of the City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """City class"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
