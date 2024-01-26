#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8), while also handling HTTPError exceptions
"""

import sys
import requests


if __name__ == "__main___":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
