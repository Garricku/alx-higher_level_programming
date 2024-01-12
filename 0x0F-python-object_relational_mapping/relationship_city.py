#!/usr/bin/python3
"""
City class definition
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
"""
Defines the imported modules
"""


class City(Base):
    """
    Defines the class city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
