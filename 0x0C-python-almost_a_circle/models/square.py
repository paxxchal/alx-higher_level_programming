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

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
