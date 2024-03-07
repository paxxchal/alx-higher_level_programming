#!/usr/bin/python3

"""
This module defines the Base class for the project.
"""


class Base:
    """
    Base class for managing id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the Base object.

        Args:
        - id (int): The identifier for the object.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
