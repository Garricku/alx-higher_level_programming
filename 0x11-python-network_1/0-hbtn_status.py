#!/usr/bin/python3
"""This module featches a URL https://alx-intranet.hbtn.io/status"""

import urllib.request
"""This module is used to work with urls for html requests & responces"""


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    web_content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(web_content)))
    print("\t- content: {}".format(web_content))
    print("\t- utf8 content: {}".format(web_content.decode('utf-8')))
