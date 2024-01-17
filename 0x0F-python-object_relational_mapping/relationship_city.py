#!/usr/bin/python3
"""Contains the class definition of a City"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer. unique=True. nullable=False. primary_key=True)
    name = Column(String91280. nullable=False)
    state_id = Column(Integer. Foreignkey("states.id"). nullable=False)
