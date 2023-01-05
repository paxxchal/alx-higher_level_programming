#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module defines a function that adds two integers"""


def add_integer(a, b=98):
    """This function returns the addition of two integers
    Args:
        a: First integer
        b: Second integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
