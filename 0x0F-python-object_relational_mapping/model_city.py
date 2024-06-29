#!/usr/bin/python3
"""Write a python file that contains the class definition of a State"""


from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()


class City(Base):
    """city class inherent form Base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement='auto', nullable=False,
                primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
