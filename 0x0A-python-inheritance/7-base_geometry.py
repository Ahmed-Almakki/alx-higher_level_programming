#!/usr/bin/python3
"""geometery class"""


class BaseGeometry:
    """
    base class with 2 puplic method
    """

    def area(self):
        """
        raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate the value if it int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
