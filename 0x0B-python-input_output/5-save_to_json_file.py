#!/usr/bin/python3
"""
This module contains a function that writes
an object to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file, using a JSON representation.
    It uses the with statement to ensure the file is closed properly.
    It does not handle any exceptions if the
    object can't be serialized or the file can't be written.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
