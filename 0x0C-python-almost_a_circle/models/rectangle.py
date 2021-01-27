#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def validation(name, value):
        """validation"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set with"""
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """height"""
        return self.__x

    @x.setter
    def x(self, value):
        """set height"""
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """height"""
        return self.__y

    @y.setter
    def y(self, value):
        """set height"""
        self.validation("y", value)
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Print"""
        print('\n' * self.__y + (' ' * self.__x + "#" * self.width +
              '\n') * self.height, end="")

    def __str__(self):
        """the string format"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the argument of Rectangle"""
        if len(args) != 0:
            atrib = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, atrib[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
