#!/usr/bin/python3
"""
contains the class definition of state and an instance of declarative_base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData


mymetadata = MetaData()
Base = declarative_base()


class State(Base):
    """ class that links to the states table in our database"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
