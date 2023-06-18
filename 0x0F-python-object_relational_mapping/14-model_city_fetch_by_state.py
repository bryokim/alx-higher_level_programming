#!/usr/bin/python3

"""Prints all City objects in the given database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased

from model_state import Base, State
from model_city import City

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

    new_table = session.query(State.name, City.id, City.name).\
        join(City).order_by(City.id).all()

    for state_name, city_id, city_name in new_table:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()
