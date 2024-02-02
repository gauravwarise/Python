name="ajay"
age=10
class info():
    name="atul"
    age=20
    def intro(self):
        return f"My name is {self.name}, my age is {self.age}"
i1=info()
print(i1.intro())
i1.age = 30
print(i1.age)