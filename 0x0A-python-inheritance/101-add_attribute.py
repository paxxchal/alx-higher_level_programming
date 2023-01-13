#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module defines a base geometry class"""


def add_attribute(obj, attr, value):
    """This function adds a new attribute to an object if it is possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
