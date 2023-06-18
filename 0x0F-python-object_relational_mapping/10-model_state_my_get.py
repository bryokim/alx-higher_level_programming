#!/usr/bin/python3

"""Print the state id of the state with the passed name"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = session.query(State.id).\
        filter(State.name == sys.argv[4]).first()

    if state_id:
        print("{}".format(state_id[0]))
    else:
        print("Not found")

    session.close()
