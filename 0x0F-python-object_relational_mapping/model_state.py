#!/usr/bin/python3
"""
Module containing the class definition of a State and an instance of Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    Class representing the State model.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)