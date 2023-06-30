#!/usr/bin/python3
"""Takes a URL and an email, sends a POST request to the URL with email as a
parameter and displays the bosy of the response."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")

    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        print(f"{response.read().decode('utf-8')}")
