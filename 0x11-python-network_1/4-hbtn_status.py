#!/usr/bin/python3
"""Script that fetche"""
import requests


if __name__ == "__main__":
    r-o = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r-o.text)))
    print("\t- content: {}".format(r-o.text))
