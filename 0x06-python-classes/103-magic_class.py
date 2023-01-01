#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module hosts a class, MagicClass"""
import math
class MagicClass:
    """This is a magic class"""
    def __init__(self, radius):
        """This function initializes the attributes
        Args: Radius"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        return self._MagicClass__radius = radius

    def area(self):
        """This function calculates the area of a circle"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """This function calculates the circumference of a circle"""
        return 2 * math.pi * self._MagicClass__radius
