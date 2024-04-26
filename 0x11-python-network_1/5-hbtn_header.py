#!/usr/bin/python3
"""
a script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


def main(url):
    """
    a script that takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id in
    the response header
    """
    response = requests.get(url)
    id_ = response.headers.get("X-Request-Id")
    print(id_)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
