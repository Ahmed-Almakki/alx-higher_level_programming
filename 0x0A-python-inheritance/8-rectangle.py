#!/usr/bin/python3
"""rectangle class"""
BaseGeometry = __import__('7-base_geometry.py').BaseGometry


class Rectangle(BaseGeometry):
    """
    chukd class inherent from geomtry
    """

    def __init__(self, width, height):
        """
        init ith arguments
        args:
            width: width of rectangle
            heigh: height of rectangke
        """
        self.__width = width
        self.__height = height
