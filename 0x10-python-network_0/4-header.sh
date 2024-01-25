#!/bin/bash
# takes in a URL, sends a GET request, displays the body of the response
curl -s -H "X-School-User-Id: 98" -X GET $1
