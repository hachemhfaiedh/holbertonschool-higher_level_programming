#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    vals = {'q': ""}
    if len(argv) == 2:
        vals['q'] = argv[1]
    re = requests.post('http://0.0.0.0:5000/search_user', data=vals)
    try:
        if not re.json():
            print("No result")
        else:
            print("[{}] {}".format(re.json().get('id'), re.json().get('name')))
    except:
        print('Not a valid JSON')
