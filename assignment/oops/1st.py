class operatoroverride:
    def __init__(self,a):
        self.a=a
    def __mult__(self,o):
        return self.a*o.a
    def __div__(self,o):
        return self.a/o.a
        
a1=operatoroverride(1)
a2=operatoroverride(5)


print(operatoroverride.__mult__(a1,a2))
print(operatoroverride.__div__(a1,a2))

