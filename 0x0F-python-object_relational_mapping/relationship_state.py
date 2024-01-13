#!/usr/bin/python3
"""
State class definition
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
"""
Defines the imported modules
"""


meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """
    Defines the class state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
