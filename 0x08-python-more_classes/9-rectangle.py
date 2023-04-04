#!/usr/bin/python3
"""
Define a class Rectangle that defines a rectangle
"""
class Rectangle:
    """
    Rectangle class

    Attributes:
    - width (int): width of the rectangle
    - height (int): height of the rectangle
    - number_of_instances (int): number of rectangle instances
    - print_symbol (any): symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializer

        Args:
        - width (int): width of the rectangle
        - height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the value of width

        Args:
        - value (int): the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of height

        Args:
        - value (int): the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        str_rect = ""
        for i in range(self.__height):
            str_rect += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                str_rect += "\n"
        return str_rect

    def __repr__(self):
        """Return formal string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area

        Args:
        - rect_1 (Rectangle): rectangle 1
        - rect_2 (Rectangle): rectangle 2

        Returns:
        - the biggest rectangle or rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with
