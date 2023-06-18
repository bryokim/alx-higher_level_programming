#!/usr/bin/python3

"""Lists all City objects from the database.

Format:
    <city id>: <city name> -> <state name>
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

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')

    session.close()
