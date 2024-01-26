#!/usr/bin/python3
"""
This module takes in a letter and sends a POST request to the following url
http://0.0.0.0:5000/search_user, with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
