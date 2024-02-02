# to overload comparison operator
class example:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
e1=example(20)
e2=example(5)

if(e1>e2):
    print("e1 is greater than e2")
else:
    print("e2 is greater than e1")