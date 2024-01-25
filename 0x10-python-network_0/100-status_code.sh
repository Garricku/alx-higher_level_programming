#!/bin/bash
# sends a request to a URL, displays only the status code of the response
curl -s -o /dev/null -w "%{http_code}" -X GET $1
