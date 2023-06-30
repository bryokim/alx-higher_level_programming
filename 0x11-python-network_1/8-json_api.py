#!/usr/bin/python3

"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as parameter"""

import requests
import sys

if __name__ == "__main__":
    try:
        payload = {"q": sys.argv[1]}
    except IndexError:
        payload = {"q": ""}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        data = r.json()
        print("[{}] {}".format(data["id"], data["name"]))
    except KeyError:
        print("No result")
    except ValueError:
        print("Not a valid JSON")
