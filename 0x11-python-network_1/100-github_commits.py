#!/usr/bin/python3
"""
This module takes 2 arguments in order to solve this challenge
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    json_data = response.json()
    for commit in json_data[:10]:
        sha = commit.get('sha')
        author_name = commit.get('name')
        print("{}: {}".format(sha, author_name))
