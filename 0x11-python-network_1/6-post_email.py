#!/usr/bin/python3

"""Takes in a URL and email address, sends a POST request to the URL
with the email as a parameter and displays the body of the response"""

import requests
import sys

if __name__ == "__main__":
    payload = {"email": sys.argv[2]}

    r = requests.post(sys.argv[1], data=payload)

    print(r.text)
