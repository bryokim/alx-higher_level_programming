#!/usr/bin/python3

"""Module for selecting cities in a state from a database"""

import MySQLdb
import sys


def get_cities_in_state():
    """Get cities from the database."""

    try:
        (username, password, db_name, state_name) = sys.argv[1:5]
    except ValueError:
        mes = "USAGE: ./5-filter_cities.py [user] [pass] [db_name] [state]"
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
        """SELECT name
        FROM cities
        WHERE state_id = (
            SELECT id
            FROM states
            WHERE name = %s
        )
        ORDER BY cities.id ASC""", (state_name,))

    states = cur.fetchall()

    if (not states):
        print()
    else:
        for i, state in enumerate(states):
            if i == len(states) - 1:
                print(state[0])
            else:
                print(state[0], end=", ")

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_cities_in_state()
