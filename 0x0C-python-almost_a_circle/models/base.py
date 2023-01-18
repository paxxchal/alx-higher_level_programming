#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
first class Base
"""


class Base:
    """This class is a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This function initializes attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
