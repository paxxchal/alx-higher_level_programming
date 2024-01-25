#!/usr/bin/python3
"""This module defines a class MagicClass."""

import math


class MagicClass:
    """This class performs operations similar to the provided bytecode."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass.

        Args:
        - radius (int or float): The radius value (default is 0).
        """
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the MagicClass."""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    # You can add any testing or demonstration code here
    pass
