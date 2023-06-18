#!/usr/bin/python3

"""Module for selecting all states from a database"""

import MySQLdb
import sys


def get_states():
    """Get all states from a database."""

    try:
        (username, password, db_name) = sys.argv[1:4]
    except ValueError:
        sys.exit("USAGE: ./0-select_states.py [username] [password] [db_name]")

    options = {
        "host": "localhost",
        "password": password,
        "user": username,
        "database": db_name
    }

    conn = MySQLdb.connect(**options)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()


if __name__ == "__main__":
    get_states()
