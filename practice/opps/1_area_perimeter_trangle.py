# Write a program to print the area and perimeter of a triangle
# having sides of 3, 4 and 5units by creating a class named 'Triangle' 
# without any parameter in its constructor.

class Triagle():
    def __init__(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def area(self):
        return self.l*self.w*self.h
    def peremiter(self):
        return self.l+self.w+self.h
        
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
ob1=Triagle(n1,n2,n3)
print(ob1.area())
print(ob1.peremiter())
