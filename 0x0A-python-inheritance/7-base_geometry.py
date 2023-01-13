#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module defines a base geometry class"""


class BaseGeometry:
    """This is an empty class"""

    def area(self):
        """This is an method raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
