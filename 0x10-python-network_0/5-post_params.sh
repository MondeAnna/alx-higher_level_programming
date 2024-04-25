#!/bin/bash
# send post request
curl  -ls -d "e-mail=test@gmail.com" -d "subject=I will always be here for PLD" -X POST "$1"
