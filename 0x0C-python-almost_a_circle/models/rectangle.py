#!/usr/bin/python3
"""This module for Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This class for Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the intialization method of class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''This is width getter decorator'''
        return self.__width

    @width.setter
    def width(self, new_value):
        '''This is width setter decoratror'''
        if type(new_value) is not int:
            raise TypeError('width must be an integer')
        if new_value <= 0:
            raise ValueError('width must be > 0')
        self.__width = new_value

    @property
    def height(self):
        '''This is heigit getter decorator'''
        return self.__height

    @height.setter
    def height(self, new_value):
        '''This is height setter decoratror'''
        if type(new_value) is not int:
            raise TypeError('height must be an integer')
        if new_value <= 0:
            raise ValueError('height must be > 0')
        self.__height = new_value

    @property
    def x(self):
        '''This x width getter decorator'''
        return self.__x

    @x.setter
    def x(self, new_value):
        '''This is x setter decoratror'''
        if type(new_value) is not int:
            raise TypeError('x must be an integer')
        if new_value < 0:
            raise ValueError('x must be >= 0')
        self.__x = new_value

    @property
    def y(self):
        '''This is y getter decorator'''
        return self.__y

    @y.setter
    def y(self, new_value):
        '''This is y setter decoratror'''
        if type(new_value) is not int:
            raise TypeError('y must be an integer')
        if new_value < 0:
            raise ValueError('y must be >= 0')
        self.__y = new_value
