#!/usr/bin/python3
"""cript that deletes all State objects with a name containing"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).filter(State.name.like("%a%")).all()
    for stat in res:
        session.delete(stat)
    session.commit()
