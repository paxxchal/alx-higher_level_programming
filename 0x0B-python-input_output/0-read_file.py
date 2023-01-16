#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines  a function
that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read())
