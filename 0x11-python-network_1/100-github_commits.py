#!/usr/bin/python3
"""
Fetches 10 most recent commits of a repository from GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = (
        f"https://api.github.com/repos/{owner_name}/"
        f"{repository_name}/commits"
    )
    response = requests.get(url)
    commits = response.json()[:10]  # Get the 10 most recent commits
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
