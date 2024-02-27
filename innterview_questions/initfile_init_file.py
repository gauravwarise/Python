'''
The __init__.py file lets the Python interpreter know that a directory contains code for a Python Module.
It can be black.
Without one, you cannot import modules from another folder into your project.

'''

'''
The __init__() method is Constructor 
This is used for initialize the objects state
'''

# A Sample class with init method
class Person:
    # init method or constructor
    def __init__(self, name):
        self.name = name
    
    # sample method
    def say_hi(self):
        print('Hello, my name is', self.name)

obj = Person('gaurav')
obj.say_hi()