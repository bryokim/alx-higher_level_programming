#!/usr/bin/python3

"""Creates the state "California" with the city "San Francisco"
and they are added to the database."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from relationship_city import City
from relationship_state import State, Base

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

    state = State(name="California")
    state.cities = [City(name="San Francisco")]

    session.add(state)
    session.commit()
    session.close()
