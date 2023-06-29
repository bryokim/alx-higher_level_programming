#!/bin/bash
# Takes a URL, sends request to URL and displays size of the response body.
curl -sI "$1" | grep -i "Content-Length" | cut -d : -f 2 | awk '{$1=$1};1'
