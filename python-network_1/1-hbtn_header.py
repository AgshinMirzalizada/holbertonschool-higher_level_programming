#!/usr/bin/python3
"""
Sends a request to the given URL and prints the value of the 'X-Request-Id' header.
"""

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
