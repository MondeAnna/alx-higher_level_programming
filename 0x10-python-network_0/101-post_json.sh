#!/bin/bash
# post json file
curl -Ls -d "$( cat "$2" )" -X "POST" "$1"
