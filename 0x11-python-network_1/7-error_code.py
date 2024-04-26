#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response
"""
from requests.exceptions import HTTPError
import requests
import sys


def main(url):
    """
    Write a Python script that takes in a URL, sends a request
    to the URL and displays the body of the response
    """
    response = requests.get(url)
    if response.status_code >= 400:
        return print(f"Error code: {response.status_code}")
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
