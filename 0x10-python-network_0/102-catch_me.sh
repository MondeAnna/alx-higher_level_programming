#!/bin/bash
# chase requests
curl -Ls --cookie "user_id=98" -X PUT "0.0.0.0:5000/catch_me"
