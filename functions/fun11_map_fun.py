# map function
# in_build function
# it will take
    # 1. function
    # 2. collection
# output will be in the form of list after type casting
x=[1,2,3,4,5]
def sq(n):
    return n**2
print("Square of number is", sq(4))
square=list(map(sq,x))
print(square)