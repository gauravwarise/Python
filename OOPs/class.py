class human():
    eyes="blue"
    hair="black"
    gender="female"

    def speak(self):
        return "I am speaking"
    def walk(self):
        return "I am walking"
obj1=human()
print(obj1.eyes)
print(obj1.hair)
print(obj1.gender)

obj2=human()
print(obj2.speak())
print(obj1.walk())