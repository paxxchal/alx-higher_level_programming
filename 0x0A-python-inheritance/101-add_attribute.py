#!/usr/bin/python3
"""Adds an attribute to an object if possible"""


def add_attribute(obj, name, value):
    """Add attribute to object if possible

    Args:
        obj: Object to add attribute to
        name: Name of attribute to add
        value: Value of attribute

    Raises:
        TypeError: If attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
