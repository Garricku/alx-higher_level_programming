#!/usr/bin/python3
"""
This module takes in a GitHub username and personal access token, uses the
GitHub API to display the user’s ID
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, passwd))
    json_data = response.json()
    print(json_data['subject_id'])
