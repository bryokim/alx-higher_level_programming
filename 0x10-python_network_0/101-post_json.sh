#!/bin/bash
# Sends a JSON POST request to a URL and displays th body of the response.
curl -s -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"
