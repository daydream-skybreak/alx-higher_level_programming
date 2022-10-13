#!/usr/bin/python3
"""
script to list all state objects
"""

if __name__ == '__main__':
    from model_state import Base, State
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    s = session.query(State).filter(State.name == argv[4]).first()
    print("Not found" if not s else "{}".format(s.id))
