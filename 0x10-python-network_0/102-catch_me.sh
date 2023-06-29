#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me
