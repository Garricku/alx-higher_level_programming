#!/usr/bin/python3
"""
State class definition
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City
"""
Defines the imported modules
"""


class State(Base):
    """
    Defines the class state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref="state", cascade="all, delete")
