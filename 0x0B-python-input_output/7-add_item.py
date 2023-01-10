#!/usr/bin/python3
"""Module for saving to json"""
import json
import os.path
import sys
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    args_list = load_from_json_file(filename)
except:
    args_list = []

for arg in argv[1:]:
    args_list.append(arg)
save_to_json_file(args_list, filename)
