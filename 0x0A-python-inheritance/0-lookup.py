#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module retrieves a list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    This function returns a list of
    available attributes and methods of an object
    """
    List = []
    for i in dir(obj):
        List.append(i)

    return List
