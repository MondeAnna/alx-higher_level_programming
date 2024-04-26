#!/usr/bin/python3
"""
a script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
import requests
import sys


def main(username, password):
    """
    a script that takes your GitHub credentials (username
    and password) and uses the GitHub API to display your
    id
    """
    url = "https://api.github.com/user"
    auth = username, password

    response = requests.get(url, auth=auth)
    print(response.json().get("id"))


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    main(username, password)
