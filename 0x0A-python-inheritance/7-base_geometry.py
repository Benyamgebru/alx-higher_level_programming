#!/usr/bin/python3
"""Module: 7-base_geometry.py"""


class BaseGeometry:
    """Class: BaseGeometry"""
    def area(self):
        """method: area()"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method: integer_validator(name, value)"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
