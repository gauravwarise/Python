'''
A Decorator is just a function that takes another function 
as an argument and some extra functionality

All of this without altering the source code of the original function
'''

def decorator_func(func):
    def wrapper_func():
        print("wrapper_func Worked")
        return func()
    print("decorator_func worked")
    return wrapper_func

def show():
    print("show Worked")

# decorator_show = decorator_func(show)
# decorator_show()


# =================== alternative ==================

# @decorator_func
def display():
    print("display worked")

# display()