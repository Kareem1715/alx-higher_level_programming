#!/usr/bin/python3
"""This Module has the child class thad drieved from parent class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    '''This class inherit from Rectangle class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor method that has special functino super()'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of instance'''
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, newSize):
        '''Setter for size'''
        if type(newSize) is not int:
            raise TypeError('width must be an integer')
        if newSize <= 0:
            raise ValueError('width must be > 0')
        self.width = newSize
        self.height = newSize

    def update(self, *args, **kwargs):
        '''Update values of attributes'''
        if args:
            # If args exists and not empty
            attr = ('id', 'size', 'x', 'y')
            for idx, val in enumerate(args):
                setattr(self, attr[idx], val)
            # My First Implementation but the above is better
            # for i in range(len(args)):
            #     setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Square instacne to dictionary"""
        return {
            'id': self.id,
            'size': self.width,
            # or self.size that call size property method that return width
            'x': self.x,
            'y': self.y
        }
