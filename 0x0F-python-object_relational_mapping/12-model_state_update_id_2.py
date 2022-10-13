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
    new_name = session.query(State).filter(State.id == '2').first()
    new_name.name = 'New Mexico'
    session.commit()
