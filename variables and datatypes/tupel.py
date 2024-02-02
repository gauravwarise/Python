from re import X
from traceback import print_tb

# methods for create tuple

mytuple=()
print(type(mytuple))

mytuple=(1,2,3)
print(mytuple)

mytuple=(1,2,'raj',3.4)
print(mytuple)

mytuple=('keyboard',[1,2,3],(65,43))
print(mytuple)


x=1,2,3
a,b,c=x
print(a)
print(b)
print(c)

x=("hello",)
print(type(x))

newtuple=(1,2,'a',3.8,'rajiv','b',6,7)
print(newtuple[4])

print(mytuple)
print(mytuple[0][3])
print(mytuple[1][1])

# negative indexing
print(newtuple[-1])
print(newtuple[-4][-2])

# slicing/
print(newtuple)
print(newtuple[1:3])
print(newtuple[:6])

# update a list in tuple/
print("udate tuple")
print(mytuple)
mytuple[1][2]=100
print(mytuple)

# join two tuples/
mytuple1=(1,2,3,4)
mytuple2=(5,6,3,7)
print(mytuple1+mytuple2)

print(("hello",2)*5)