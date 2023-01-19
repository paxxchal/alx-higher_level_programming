#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This module defines the class Rectangle
that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """This class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function initializes attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) == False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) == False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int) == False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int) == False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
