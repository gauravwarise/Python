class A():
    def a(self):
        print("i an class A function")

class B():
    def a(self):
        print("i an class B function")

class C(A,B):
    pass

c = C()
B.a(c)