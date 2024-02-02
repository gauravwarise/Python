class animal():
    def walk(self):
        return "Animal is walking"
class dog(animal):
    def bark(self):
        return "Dog is barking"
class dogchild(dog):
    def sleep(self):
        return "Dog child is sleeping"
d1=dogchild()
print(d1.walk())
print(d1.sleep())
print(d1.bark())
    