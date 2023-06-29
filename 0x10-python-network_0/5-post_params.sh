#!/bin/bash
# Takes a URl, sends a POST request to the URL and displays the body of the response.
curl -s --data-raw "email=test@gmail.com" -d "subject=I will always be here for PLD" -X "POST" "$1"
