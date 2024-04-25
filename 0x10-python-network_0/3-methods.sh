#!/bin/bash
# display allowed methods
curl -sI "$1" | grep Allow: | cut -d " " -f 2-
