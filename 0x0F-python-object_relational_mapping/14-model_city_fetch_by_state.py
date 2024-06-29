#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1],
                           sys.argv[2],
                           sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City, State) \
                 .filter(City.state_id == State.id) \
                 .order_by(City.id)
    for i, j in res:
        print("{}: ({}) {}".format(j.name, i.id, i.name))
