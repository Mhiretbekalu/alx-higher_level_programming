#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry:
    """
    add public instance method:
            def integer_validator(self, name, value):
    """
    def area(self):
        """
        method area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method: integer_validator(self, name, value)
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
