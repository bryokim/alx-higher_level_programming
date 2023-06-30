#!/usr/bin/python3
"""Takes a URL and displays the value of the X-Request-Id variable
in the header of the response"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        _headers = response.headers._headers

        for item in _headers:
            if item[0] == "X-Request-Id":
                print(item[1])
                break
