#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body
curl -s -w "%{http_code}" -X GET $1 | grep -q 200 && curl -s -X GET $1 | tail -n +11; echo -n 'Route 2'
