#!/bin/bash
#script that takes in a URL and displays all HTTP methods the server
curl -s -X OPTIONS "$1" -i | grep "Allow" | cut -d ":" -f 2
