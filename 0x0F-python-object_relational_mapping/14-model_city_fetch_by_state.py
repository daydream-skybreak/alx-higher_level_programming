#!/usr/bin/python3
"""
prints all city objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_city import City
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in objs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
