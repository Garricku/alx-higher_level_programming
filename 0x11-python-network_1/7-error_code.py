#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8), while also handling HTTPError exceptions
"""

import sys
import requests


if __name__ == "__main___":
    url = sys.argv[1]
    response = requests.get(url)
    response.raise_for_status()
    if e.response.status_code >= 400:
        print("Error code: {}".format(e.response.status_code))
    else:
        print(response.text)
