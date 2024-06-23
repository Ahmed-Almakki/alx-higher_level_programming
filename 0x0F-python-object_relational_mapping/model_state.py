#!/usr/bin/python3
"""Write a python file that contains the class definition of a State"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()

class State(Base):
    """ state class thats gona be a database"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement='auto')
    name = Column(String(128), nullable=False)
