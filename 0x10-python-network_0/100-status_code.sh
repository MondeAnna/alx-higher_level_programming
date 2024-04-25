#!/bin/bash
# request status code
curl -so /dev/null --head -w "%{http_code}" "$1"
