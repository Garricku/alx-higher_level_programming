#!/usr/bin/python3
"""Defines the module rectangle."""


from models.base import Base
"""Defines the imported modules."""


class Rectangle(Base):
    """Defines the subclass Rectangle, which inherits from Base."""

    def __init__(self, width, height, x=0,y=0, id=None):
        """Defines a constructor for the Rectangle class."""

        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

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


    @property
    def width(self):
        """Defines the getter method for width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Defines the setter for width in which value is set to the width."""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value


    @property
    def height(self):
        """Defines the getter method for height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the setter for height in which value is set to the height."""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value


    @property
    def x(self):
        """Defines the getter method for x."""

        return self.__x

    @x.setter
    def x(self, value):
        """Defines the setter for x in which value is set to x."""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value


    @property
    def y(self):
        """Defines the getter method for y."""

        return self.__y

    @y.setter
    def y(self, value):
        """Defines the setter for y in which value is set to y."""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Defines a method that returns the area value of the class object."""

        return self.__width * self.__height


    def display(self):
        """Defines a method that prints the class object with a # to stdout."""

        for row in range(self.__y):
            print()

        for y_axis in range(self.__height):
            for collumn in range(self.__x):
                print(" ", end="")
            print("#", end="")

            for x_axis in range(1, self.__width):
                print("#", end="")
                if x_axis == self.__width - 1:
                    print()


    def __str__(self):
        """Defines the override of the magic method __str__."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)


    def update(self, *args, **kwargs):
        """Defines a method that updates values via the cmd line args input."""

        if len(args) >= 1:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) >= 2:
            self.__width = args[1]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) >= 3:
                self.__height = args[2]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) >= 4:
            self.__x = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Defines a method that returns a Rectangle as a dictionary."""

        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
