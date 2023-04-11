#!/usr/bin/python3
"""Module documentation.

This module creates a class that inherits from list and has an additional
public instance method to print the sorted list.

"""
class MyList(list):
    """Class documentation.

    This class inherits from the built-in list class and has an additional
    public instance method to print the sorted list.

    """
    def print_sorted(self):
        """Method documentation.

        This method prints the sorted list in ascending order.

        """
        print(sorted(self))

