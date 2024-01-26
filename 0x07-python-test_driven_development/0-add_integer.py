#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: First integer
    :param b: Second integer (default is 98)
    :return: Sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
