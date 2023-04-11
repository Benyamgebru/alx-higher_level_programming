#!/usr/bin/python3
"""Module defines a Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle

        Raises:
        TypeError: If width or height are not integers
        ValueError: If width or height are <= 0
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of a Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
