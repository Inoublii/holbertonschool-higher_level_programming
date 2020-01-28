#!/usr/bin/python3
'''import Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """define Square """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''Square str'''
        return ("[Square](%s) %s/%s - %s" % (self.id,
                                             self.x,
                                             self.y,
                                             self.size))

    def update(self, *args, **kwargs):
        """updare def"""
        if "id" in kwargs:
            self.id = kwargs["id"]
        elif len(args) > 0:
            self.id = args[0]
        if "size" in kwargs:
            self.size = kwargs['size']
        elif len(args) > 1:
            self.size = args[1]
        if "x" in kwargs:
            self.x = kwargs["x"]
        elif len(args) > 2:
            self.x = args[2]
        if 'y' in kwargs:
            self.y = kwargs['y']
        elif len(args) > 3:
            self.y = args[3]

        def to_dictionary(self):
            """dictionairy"""
            dic = {
                "id": self.id, "size": self.size,
                "x": self.x, "y": self.y,
            }
            return (dic)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value
