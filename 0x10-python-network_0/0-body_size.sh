#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
response=$(curl -s "$1")
size=$(echo "$response" | wc -c)
echo "Size of the response body: $size"
