#!/usr/bin/python3
"""Write a script that prints the first State"""
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
    result = session.query(State.id, State.name).filter(State.id==1)
    for results in result:
        print("{1}: {0}".format(results.name, results.id))
    session.close()
