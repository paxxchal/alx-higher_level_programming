#!/usr/bin/python3
# This is a Python function that does
# exactly the same as the given Python bytecode.
def magic_calculation(a, b, c):
    """This function takes three numbers
    as arguments and returns a value based on some conditions."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
