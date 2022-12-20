#!/usr/bin/python3
"""
defining a class Mylist
"""


class MyList(list):
    """declare func that prints list"""

    def print_sorted(self):
        print(sorted(self))
