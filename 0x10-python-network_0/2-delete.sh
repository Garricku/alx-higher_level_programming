#!/bin/bash
# Write a Bash script that sends a DELETE request to the URL
curl -s -X DELETE $1; echo -n "I'm a DELETE request"
