#!/usr/bin/python3


def raise_exception():
    try:
        raise TypeError("This is a custom type exception.")
    except TypeError as e:
        print(f"Exception raised: {e}")
