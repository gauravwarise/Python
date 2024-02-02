class mom():
    eyes="blue"
    hair="brown"
    nose="long and straight"

    def intro(self):
        return "I am mom class"
class child(mom):
    def intro(self):
        return " I am child class"
c1=child()
print(c1.eyes)
print(c1.intro())
