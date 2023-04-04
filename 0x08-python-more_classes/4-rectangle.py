#!/usr/bin/python3
"""
This module contains a class Rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes an object for the Rectangle class.

        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter function for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for width attribute.

        Args:
        value (int): value to set width to.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter function for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for height attribute.

        Args:
        value (int): value to set height to.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Method to calculate the area of the Rectangle object.

        Returns:
        int: area of the Rectangle object.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method to calculate the perimeter of the Rectangle object.

        Returns:
        int: perimeter of the Rectangle object.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Method to print a rectangle using the '#' character.
        """
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return rect_str
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        Method to return a string representation of the Rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
