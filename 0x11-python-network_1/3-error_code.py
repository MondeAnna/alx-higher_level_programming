#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


def main(url):
    """
    Write a Python script that takes in a URL, sends a request
    to the URL and displays the body of the response (decoded
    in utf-8)
    """
    try:
        with urlopen(url) as resp:
            response = resp.read()
    except HTTPError as error:
        print(f"Error code: {error.code}")
        return

    print(f"{str(response, 'utf-8')}")


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
