#!/usr/bin/python3
"""A class that defines a rectangle."""

class Rectangle:
    """A class that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""

        rect_str = ""

        for i in range(self.height):
            rect_str += str(Rectangle.print_symbol) * self.width + "\n"

        return rect_str[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle to recreate it."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
      print("Bye rectangle...")
      Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
      if not isinstance(rect_1, Rectangle):
          raise TypeError("rect_1 must be an instance of Rectangle")
      if not isinstance(rect_2, Rectangle):
          raise TypeError("rect_2 must be an instance of Rectangle")
      if rect_1.area() >= rect_2.area():
          return rect_1
      else:
          return rect_2

if __name__ == '__main__':
    pass
