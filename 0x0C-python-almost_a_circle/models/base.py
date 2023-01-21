#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
first class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
