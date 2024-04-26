#!/usr/bin/python3
"""script to fetch from https://alx-intranet.hbtn.io/status"""
import requests


def main():
    """script to fetch from https://alx-intranet.hbtn.io/status"""
    url = "https://alx-intranet.hbtn.io/status"
    text = requests.get(url).text
    print(
        "Body response:\n" +
        f"\t- type: {type(text)}\n" +
        f"\t- content: {text}"
    )


if __name__ == "__main__":
    main()
