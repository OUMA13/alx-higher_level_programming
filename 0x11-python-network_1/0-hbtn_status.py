#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", utf8_content)

