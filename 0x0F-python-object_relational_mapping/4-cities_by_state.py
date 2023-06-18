#!/usr/bin/python3

"""Module for selecting cities from a database"""

import MySQLdb
import sys


def get_cities():
    """Get cities from the database."""

    try:
        (username, password, db_name) = sys.argv[1:4]
    except ValueError:
        mes = "USAGE: ./4-cities_by_state.py [user] [pass] [db_name]"
        sys.exit(mes)

    options = {
        "host": "localhost",
        "password": password,
        "user": username,
        "database": db_name
    }

    conn = MySQLdb.connect(**options)
    cur = conn.cursor()
    cur.execute(
        """SELECT id, city_name, state_name
        FROM (
            SELECT c.id AS id, c.name AS city_name, s.name AS state_name
            FROM cities c
                INNER JOIN states s ON c.state_id = s.id
        )X
        ORDER BY id ASC""")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_cities()
