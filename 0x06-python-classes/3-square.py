#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module hosts a class, Square that defines a square"""


class Square:
    """This class describes a square"""

    def __init__(self, size=0):
        """The init function to initialize instance attributes
        Args:
            size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """The area function calculates the area of the current square
        Return:
            self.__size ** 2 which gives the area of the circle
        """
        return self.__size**2
