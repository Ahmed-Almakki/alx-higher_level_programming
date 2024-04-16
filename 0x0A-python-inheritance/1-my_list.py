#!/usr/bin/python3
"""child class Mylist inerent from list"""


class MyList(list):
    """
    child class
    """

    def print_sorted(self):
        """
        method sort a list
        """
        print(sorted(self))

