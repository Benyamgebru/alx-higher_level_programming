#!/usr/bin/python3
"""
Module that contains the `BaseGeometry` class and `Rectangle` subclass
"""


class BaseGeometry:
    """
    Class with area method and integer validator
    """

    def area(self):
        """
        Raises an exception since this method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class that inherits from `BaseGeometry` class and represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the `Rectangle` class.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of a `Rectangle` instance.

        Returns:
            str: a string representation of the `Rectangle` instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
