class addition():
    def add(self,a,b):
        sum=a+b
        return sum
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
sum=addition()
print("Addition of number is: ",sum.add(x,y))