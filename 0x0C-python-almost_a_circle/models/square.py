#!/usr/bin/python3
""" Class: Square """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class: Square of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiate size, x, y, id """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of the class """
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y,
                                                       self.width)

    @property
    def size(self):
        """ Property getter for size """
        return self.width

    @size.setter
    def size(self, size):
        """Setter method to size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the argument of Square"""
        if len(args) != 0:
            lista = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, lista[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance """
        ret_dict = {}
        ret_dict['id'] = self.id
        ret_dict['x'] = self.x
        ret_dict['y'] = self.y
        ret_dict['size'] = self.size

        return ret_dict
