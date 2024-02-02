# to overload binary + operator
class addition:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a#to add two objects

    # def __add__(self,other):
    #     a=self.a+other.a 
    #     return addition(a)
    


a1=addition(1)
a2=addition(5)

a3=addition("welcome")
a4=addition(" ITVedant")

print(a1+a2)
print(a3+a4)

print(addition.__add__(a1,a2))
print(addition.__add__(a3,a4))

print(a1.__add__(a2))
print(a3.__add__(a4))