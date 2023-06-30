#!/usr/bin/python3
"""Lists last 10 commits (from the most recent to oldest) of
the repository "rails" by the user "rails".
Format:
    <sha>: <author name>
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(
            "https://api.github.com/repos/{}/{}/commits".format(
                sys.argv[2], sys.argv[1])
        )

    commits = r.json()

    for i, commit in enumerate(commits):
        if i < 10:
            print("{}: {}".format(
                commit["sha"], commit["commit"]["author"]["name"])
            )
        else:
            break
