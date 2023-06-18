#!/usr/bin/python3

"""Module for selecting states with given name from a database"""

import MySQLdb
import sys


def get_named_state():
    """Get state with given name from a database."""

    try:
        (username, password, db_name, state_name) = sys.argv[1:5]
    except ValueError:
        mes = "USAGE: ./2-my_filter_states.py [user] [pass] [db_name] [state]"
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
        """SELECT * FROM states
        WHERE name = %s
        ORDER BY id""", (state_name,))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_named_state()
