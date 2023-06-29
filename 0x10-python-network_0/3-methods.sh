#!/bin/bash
# Takes URL and displays all HTTP methods the server will accept.
curl -sI -X "OPTIONS" "$1" | grep -w "Allow" | cut -d : -f 2 | awk '{$1=$1};1'
