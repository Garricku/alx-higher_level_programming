#!/usr/bin/python3
"""Defines a module square."""


from models.rectangle import Rectangle
"""Defines the imported modules."""


class Square(Rectangle):
    """Defines the subclass Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Defines the constructor for the Square class."""

        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = size
            self.__height = size

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
            super().__init__(size, size, x, y, id)


    def __str__(self):
        """Defines a magic method that overrides other str magic methods."""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x,
                self.__y, self.__width)


    @property
    def size(self):
        """Defines the getter method for the size attribute."""

        return self.__width

    @size.setter
    def size(self, value):
        """Defines the setter method for the size attribute."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """Defines the update method that updates the class Square's values."""

        if len(args) >= 1:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) >= 2:
            self.__width = args[1]
            self.__height = args[1]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) >= 3:
                self.__x = args[2]
        else:
            for key, value in kwargs.items():
                if key == "x":
                    self.__x = value

        if len(args) >= 4:
            self.__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Defines a method that returns a Square object as a dictionary."""

        return {'id': self.id, 'size': self.__width, 'x': self.__x,
                'y': self.__y}
