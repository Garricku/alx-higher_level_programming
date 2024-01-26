#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as req:
    print(req.getheader('X-Request-Id'))
