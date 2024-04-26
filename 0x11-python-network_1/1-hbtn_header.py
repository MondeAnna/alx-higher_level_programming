#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
value of the `X-Request-Id` variable found in the header of the response
"""
from urllib.request import urlopen
import sys


def main(url):
    """
    script that takes in a URL, sends a request to the
    URL and displays the value of the `X-Request-Id`
    variable found in the header of the response
    """

    with urlopen(url) as response:
        _id = response.getheader("X-Request-Id")
        print(_id)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
