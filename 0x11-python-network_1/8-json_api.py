#!/usr/bin/python3
"""
Write a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import sys


def main(query):
    """
    Write a Python script that takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter
    """
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": query}

    response = requests.get(url, params=params)
    json_ = response.json()

    if not json_:
        return print("No result")

    id_ = json.get("id")
    name = json.get("name")

    print(f"[{id_}] {name}")


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) == 2 else ""
    main(query)
