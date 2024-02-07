#!/usr/bin/python3
"""
This module contains a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file.
    It uses the with statement to ensure the file is closed properly.
    It does not handle any exceptions if the
    JSON string does not represent an object.
    It returns the object created from the JSON file.
    """
    with open(filename, "r") as f:
        return json.load(f)
