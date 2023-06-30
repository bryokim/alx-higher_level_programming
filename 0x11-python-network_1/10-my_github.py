#!/usr/bin/python3
"""Takes GitHub credentials (username and password) and uses
Github API to display your id"""

import requests
import sys

if __name__ == "__main__":
    headers = {"Authorization": f"Bearer {sys.argv[2]}"}

    r = requests.get(
            f"https://api.github.com/users/{sys.argv[1]}",
            headers=headers
        )

    print(r.json().get("id"))
