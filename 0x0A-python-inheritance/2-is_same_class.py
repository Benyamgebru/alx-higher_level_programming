#!/usr/bin/python3
"""Defines a class-checking function."""

def is_same_class(obj. a_class):
    """check if an object is exactly an instance of a given class.

    Args:
    obj: object to check
    a_class: specified class

Returns:
    True if obj is exactly an instance of a_class, False otherwise.
"""
return type(obj) is a_class
