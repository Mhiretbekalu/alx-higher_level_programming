#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """
    attributes:
        width, height
    methods:
        getter and setter methods for height and width
    """
    def __init__(self, width=0, height=0):
        """inistantiate width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter method to return width instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method to set width to value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to return height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to set height to value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectanlge"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """return readable string"""
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            rectangle += ("#" * self.__width)
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """returns instance of rect using eval"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a text when instance of rectangle is deleted"""
        print("Bye rectangle...")
