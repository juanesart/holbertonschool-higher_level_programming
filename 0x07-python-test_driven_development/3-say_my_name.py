#!/usr/bin/python3
"""
"3-say_my-name" module.
Function: print a string with two parameters.
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is" followed by the first name and optional last name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
