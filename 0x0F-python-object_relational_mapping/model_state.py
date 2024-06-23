#!/usr/bin/python3
"""Write a python file that contains the class definition of a State"""
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER
import sys


Base = declarative_base()

class State(Base):
    """ state class thats gona be a database"""
    __tablename__ = "states"

    id = Column(INTEGER(display_width=11), primary_key=True, nullable=False,
                autoincrement='auto')
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], 
        sys.argv[2], 
        sys.argv[3]), 
        pool_pre_ping=True)
Base.metadata.create_all(engine)
