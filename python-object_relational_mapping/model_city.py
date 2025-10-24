#!/usr/bin/python3
"""
File containing the class for defining a city
"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class
    """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State")
