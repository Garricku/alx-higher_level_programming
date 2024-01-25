#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body
response=$(curl -s -w "%{http_code}" -X GET $1 -o /dev/null); echo "$response"
