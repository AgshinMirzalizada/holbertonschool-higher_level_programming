#!/usr/bin/python3
"""
Fetches data from https://intranet.hbtn.io/status using the urllib package
and displays the response body in a specific format.
"""
import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as request:
    content = request.read()

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
