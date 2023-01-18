#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
first class Base
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if not id == None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
