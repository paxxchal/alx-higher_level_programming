#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Initialize two variables to store
    # the first and second elements of each tuple
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0
    # Check the length of each tuple and assign the values accordingly
    if len(tuple_a) > 0:
        a1 = tuple_a[0]
        if len(tuple_a) > 1:
            a2 = tuple_a[1]
    if len(tuple_b) > 0:
        b1 = tuple_b[0]
        if len(tuple_b) > 1:
            b2 = tuple_b[1]
    # Add the corresponding elements of each tuple and return a new tuple
    return (a1 + b1, a2 + b2)
