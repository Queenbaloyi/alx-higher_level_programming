#!/usr/bin/python3
"""Defining a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a Circle.

        Arg:
            radius (float or int): The radius of the new Circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the Circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the Circle."""
        return (2 * math.pi * self.__radius)
