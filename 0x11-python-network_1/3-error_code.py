#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from urllib.error import HTTPError
from urllib import request
from sys import argv


if __name__ == "__main__":
    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
