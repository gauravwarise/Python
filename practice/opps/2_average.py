# Print the average of three numbers entered by user by creating a
# class named 'Average'having a method to calculate and print the average.

class Average():
    def __init__(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    def ave(self):
        return (self.n1+self.n2+self.n3)/3
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

ob1=Average(num1,num2,num3)
print("Average of number is: ", ob1.ave())