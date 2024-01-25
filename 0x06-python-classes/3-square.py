#!/usr/bin/python3
"""This module defines a class Square with private instance attribute size
and a public instance method area."""


class Square:
    """
    This class defines a square.

    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size=0): Initializes a new instance of the Square class.
    - area(self): Returns the current square area.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (int): The size of the square (default is 0).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area."""
        return self.__size**2
