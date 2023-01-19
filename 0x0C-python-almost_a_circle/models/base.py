#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
first class Base
"""


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id):
        """This function initializes attributes"""
        if id is not None:
            self.id = id
        elif id == None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
            self.id = id
