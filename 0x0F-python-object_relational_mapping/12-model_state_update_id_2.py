#!/usr/bin/python3
"""script that changes the name of a State object from the database"""
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
    res = session.query(State).filter_by(id=2).first()
    res.name = "New Mexico"
    session.commit()
