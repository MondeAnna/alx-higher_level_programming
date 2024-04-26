#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen
import sys


def main(url, email):
    """
    script that takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    unencoded_data = {"email": email}
    data = urlencode(unencoded_data).encode("ascii")

    headers = {"User-Agent": "Mozilla/5.0"}

    request = Request(url, data, headers)

    with urlopen(request) as resp:
        response = resp.read()

    print(f"{str(response, 'utf-8')}")


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    main(url, email)
