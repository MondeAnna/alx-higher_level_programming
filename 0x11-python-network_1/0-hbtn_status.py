#!/usr/bin/python3
"""script to fetch from https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen


def main():
    """script to fetch from https://alx-intranet.hbtn.io/status"""
    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as response:
        status = response.read()

    print(
        "Body response:\n" +
        f"\t- type: {type(status)}\n" +
        f"\t- content: {status}\n" +
        f"\t- utf8 content: {str(status, 'utf-8')}"
    )


if __name__ == "__main__":
    main()
