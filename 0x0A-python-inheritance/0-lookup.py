#!/usr/bin/python3
"""This module defines a lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
