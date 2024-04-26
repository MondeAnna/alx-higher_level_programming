#!/usr/bin/python3
"""
a script that lists 10 commits (from the most recent
to oldest) of the a repo. Commits are all printed by:
    `<sha>: <author name>` (one by line)
"""
import requests
import sys


def main(repo, owner):
    """
    a script that lists 10 commits (from the most recent
    to oldest) of the a repo. Commits are all printed by:
        `<sha>: <author name>` (one by line)
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    commits = requests.get(url).json()

    for commit in commits[:10]:
        author = commit["commit"]["author"]["name"]
        sha = commit["sha"]
        print(f"{sha}: {author}")


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    main(repo, owner)
