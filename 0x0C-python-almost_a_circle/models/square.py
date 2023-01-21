#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module defines the class Rectangle
that inherits from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        uses the logic of the __init__ of the Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
