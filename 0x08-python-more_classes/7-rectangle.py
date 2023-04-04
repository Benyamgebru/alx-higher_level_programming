#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """
    Rectangle Class
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Rectangle instance with width and height
        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        Args:
            value (int): Width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        Args:
            value (int): Height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate perimeter of Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Print rectangle with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width] * self.__height)

    def __repr__(self):
        """
        Return string representation of rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Delete rectangle and print Bye message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
