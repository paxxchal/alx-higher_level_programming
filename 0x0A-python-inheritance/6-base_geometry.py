#!/usr/bin/python3
"""BaseGeometry class with area() method"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")
