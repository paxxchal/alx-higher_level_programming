#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module defines a class rectangle"""


class Rectangle:
    """This class describes a rectangle"""

    def __init__(self, width=0, height=0):
        """This method sets the instance attributes
        Args:
            __width: width of the triangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle to be an integer above 0"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle to be an integer above 0"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
