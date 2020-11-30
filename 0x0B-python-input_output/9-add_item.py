#!/usr/bin/python3
"""input output"""
from sys import argv
a = __import__("7-save_to_json_file").save_to_json_file
b = __import__("8-load_from_json_file").load_from_json_file


try:
    list = b("add_item.json")

except Exception:
    list = []

list += argv[1:]
a(list, "add_item.json")
