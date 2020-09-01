#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    page = 'https://api.github.com/user'
    re = requests.get(page, auth=(argv[1], argv[2]))
    print(re.json().get('id'))
