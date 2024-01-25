#!/usr/bin/python3
"""This module defines a class Square with private instance attribute size,
a getter, a setter, and a public instance method area."""


class Square:
    """
    This class defines a square.

    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size=0): Initializes a new instance of the Square class.
    - size(self): Getter method to retrieve the size.
    - size(self, value): Setter method to set the size.
    - area(self): Returns the current square area.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.

        Args:
        - value (int): The size value to be set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size**2
