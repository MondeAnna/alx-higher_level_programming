#!/bin/bash
# send GET request
curl -Ls -H "X-School-User-Id: 98" -X "GET" "$1"
