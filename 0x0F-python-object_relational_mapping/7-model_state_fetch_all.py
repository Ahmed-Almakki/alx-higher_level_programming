#!/usr/bin/python3
"""Write a script that lists all State objects from the database"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], 
        sys.argv[2], 
        sys.argv[3]), 
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name, State.id).order_by(State.id)
    for row in result:
        print("{}: {}".format(row.id, row.name))