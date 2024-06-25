#!/usr/bin/python3
"""writ script that lists all state"""
from sqlalchemy import create_engine, insert
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1],
                           sys.argv[2],
                           sys.argv[3],),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    result = session.query(State.id, State.name)
    session.add(new)
    session.commit()
    for row in result:
        pass
    print(row.id)
