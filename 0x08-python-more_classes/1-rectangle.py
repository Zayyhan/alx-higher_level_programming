#!/usr/bin/python3

"""Defines class Rectangles"""


class Rectangle:
    """Representation of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle

            Args:
                width (int): Width of rectangle
                height (int): height if rectangle
        """
        self.height = height
        self.width = width

        @property
        def width(self):
            """retrieve width of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif width < 0:
                raise ValueError("width must be >= 0")
            self.width = value

            @property
            def height(self):
                """retrieve height of rectangle"""
                return self.__height

            @height.setter
            def height(self, value):
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                elif height < 0:
                    raise ValueError("height must be >= 0")
                self.height = value
