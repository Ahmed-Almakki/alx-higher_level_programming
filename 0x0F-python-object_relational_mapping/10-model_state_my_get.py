#!/usr/bin/python3
"""Write a script that prints the State object with the name"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1],
                           sys.argv[2],
                           sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.id, State.name).all()
    lis = {r[1]: r[0] for r in results}
    argv = sys.argv[4]
    if argv in list(lis.keys()):
        for a, b in lis.items():
            if argv == a:
                print(b)
    else:
        print("Not found")
