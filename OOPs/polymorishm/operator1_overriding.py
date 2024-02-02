class bubble():
    def __init__(self,volume):
        self.volume=volume
    def __str__(self):
        return "Volume is: "+str(self.volume)
    def __add__(self,other):
        volume=self.volume+other.volume #volume=b1+b2
        return bubble(volume)

ob1=bubble(10) #it will call constructor to initialize object
ob2=bubble(20)
print(ob1+ob2)
print(ob1)



