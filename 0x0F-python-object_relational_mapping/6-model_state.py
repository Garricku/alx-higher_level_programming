#!/usr/bin/python3
"""
Defines the module 7-model_state_fetch_all
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
"""
Defines the imported modules
"""


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://\
                           {}:{}@localhost/{}'.format(sys.argv[1],
                           sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
