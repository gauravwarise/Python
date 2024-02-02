class calc1():
    def add(self,a,b):
        return a+b
class calc2():
    def sub(self,a,b):
        return a-b
class newcalc(calc1,calc2):
    def mult(self,a,b):
        return a*b
n1=newcalc()
print(n1.add(10,20))
print(n1.sub(44,30))
print(n1.mult(10,5))