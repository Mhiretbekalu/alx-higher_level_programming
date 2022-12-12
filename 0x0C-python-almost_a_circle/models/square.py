#!/usr/bin/python3
"""
And now, the Square!
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        function
        :param size:
        :param x:
        :param y:
        :param id:
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        function: update square
        """
        for arg in args:
            i = args.index(arg)
            while i < len(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.x = arg
                else:
                    self.y = arg
                i += 1
        for key, value in kwargs.items():
            if key == "size":
                self.width = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
            elif key == "id":
                self.id = value

    def to_dictionary(self):
        """
        list out dictionary
        :return:
        """
        dic = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.height
        }
        return dic
