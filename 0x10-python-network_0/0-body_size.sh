#!/usr/bin/bash
# Takes in a URL, request that URL, displays the body size of the response
responce=$(curl -s -w "%{size_download}" -o /dev/null $1); echo "$responce"
