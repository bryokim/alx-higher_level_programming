#!/usr/bin/python3

"""Lists all State objects and corresponding City objects from
the database.

Format:
    <state id>: <state name>
    <tabulation><city id>: <city name>
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')

    session.close()
