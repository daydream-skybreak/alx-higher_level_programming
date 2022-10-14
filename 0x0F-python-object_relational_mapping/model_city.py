#!/usr/bin/python3
"""
class definition of cities
class attributes:
    id - auto-generated unique integer which cannot be null(Integer)
    name - 128 characters and cannot be null(String)
    state_id - foreign key to state.id and cannot be null(Integer)
"""

from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey



class City(Base):
    """ class that defines a city table in our database """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)