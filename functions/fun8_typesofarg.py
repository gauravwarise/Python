# required arg
def addition(x,y):
    print(x)
    print(y)
    z=x+y
    print("Addtion is",z)
addition(10,20)

# default arg
def add(a,b=10):
    print(a)
    print(b)
    c=a+b
    print("summition is",c)
add(20,50)
add(20)

# key value pair arg 
def add(a,b=10):
    print(a)
    print(b)
    c=a+b
    print("summition is",c)
add(a=20,b=50)
add(b=20,a=80)