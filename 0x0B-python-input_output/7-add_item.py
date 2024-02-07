#!/usr/bin/python3
"""Script to add arguments to a Python list and save them to a file."""

import sys
from os import path

# Add the current directory to sys.path
sys.path.append(path.0x0B-python-input_output(path.abspath(__file__)))

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_item(args):
    """Add arguments to a Python list and save them to a file.

    Args:
        args (list): List of arguments to add to the Python list.
    """
    filename = "add_item.json"

    # Check if the file exists, if not, create it
    if not path.exists(filename):
        save_to_json_file([], filename)

    # Load the existing list from the file
    existing_list = load_from_json_file(filename)

    # Add new arguments to the list
    existing_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(existing_list, filename)

if __name__ == "__main__":
    # Skip the first argument (script name) and pass the rest to add_item
    arguments = sys.argv[1:]
    add_item(arguments)
