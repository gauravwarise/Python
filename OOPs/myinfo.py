class myinfo():
    def createname(self,name):
        self.name=name
    def display(self):
        return self.name
    def helloinfo(self):
        return f"hello {self.name}"
m1=myinfo()
m2=myinfo()

m1.createname('Gaurav')
print(m1.display())
print(m1.helloinfo())