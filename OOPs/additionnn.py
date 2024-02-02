# class calc():
#     def get(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
# obj1=calc()
# obj1.get(10,20)
# print(obj1.add())


class addition():
    def get(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        sum=self.a+self.b
        return sum
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
sum=addition()
sum.get(x,y)
print("Addition of number is: ",sum.add())