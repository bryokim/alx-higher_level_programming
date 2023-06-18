#!/usr/bin/python3

"""Module for selecting states starting with N from a database"""

import MySQLdb
import sys


def get_states_start_with_N():
    """Get all states starting with N from a database."""

    try:
        (username, password, db_name) = sys.argv[1:4]
    except ValueError:
        sys.exit("USAGE: ./1-filter_states.py [username] [password] [db_name]")

    options = {
        "host": "localhost",
        "password": password,
        "user": username,
        "database": db_name
    }

    conn = MySQLdb.connect(**options)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N.*' ORDER BY id")
    states = cur.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_states_start_with_N()
