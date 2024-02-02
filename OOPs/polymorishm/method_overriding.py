class A:
    def info(self,name,age):
        self.name=name
        self.age=age
        return f"name is {self.name},age is {self.age}"
class B(A):
    def info(self,ID):
        self.ID=ID
        return f"ID is {self.ID}"
class C(A):
    def Display(self,phone):
        self.phone=phone
        return f"Phone number is {self.phone}"

obj1=C()
print(obj1.Display(123456))
print(obj1.info("gaurav",20))
obj2=B()
print(obj2.info("ID101"))
# print(obj2.info("gaurav",20))