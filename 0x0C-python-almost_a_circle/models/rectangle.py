#!/usr/bin/python3
"""
First Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """ hight setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """ prints rectangle in stdout """
        for m in range(self.__y):
            print()

        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ update rectangle """
        for arg in args:
            i = args.index(arg)
            while i < len(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                else:
                    self.__y = arg
                i += 1
        for key, value in kwargs.items():
            if key == "height":
                self.__height = value
            elif key == "width":
                self.__width = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value
            elif key == "id":
                self.id = value

    def to_dictionary(self):
        """ list out dictionary"""
        dic = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'width': self.__width,
            'height': self.__height
        }
        return dic
