#!/usr/bin/python3
"""
Defines the script 9-model_state_filter_a that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
"""
Defines the imported modules
"""


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State
                                         .name.like('%a%')).order_by(State.id)\
                    .all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
