class Employee():
    #this is parent/base/super class"
    emp_count=0#class attribute
    sal_incr=1.10
    def __init__(self,first,last,sal):
        self.first=first
        self.last=last
        self.sal=sal
    
        self.email=first.lower()+"."+last.lower()+"@gmail.com"#abc.xyz@gmail.com
        Employee.emp_count+=1#Employee.emp_count=Employee.emp_count+1
        
    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"
    def sal_increment(self):
        self.sal=self.sal*Employee.sal_incr#self.sal=10000*1.10
        return self.sal
 
class developer(Employee):
    sal_incr=1.30
    def __init__(self,first,last,sal,prolang):
        super().__init__(first,last,sal) 
        self.prolang=prolang

class Manager(Employee):
    def __init__(self,first,last,sal,emps=None):
        super().__init__(first,last,sal) 
        
        if emps is None:
            self.emps=[]
        else:
            self.emps=emps
    def addemp(self,empl):
        if empl not in self.emps:
            self.emps.append(empl)
    def removeemp(self,empl):
        if empl in self.emps:
            self.emps.remove(empl)
    def printemp(self):
        for empl in self.emps:
            print(f"--->{empl.fullname()}")
    
emp1=Employee("raj","joshi",20000)
emp2=Employee("Anita","Roy",40000)
emp3=Employee("Ram","Kumar",10000)

mgr1=Manager('Meera','Patil',80000,[emp1,emp2,emp3])

dev1=developer("raju","josh",20000,'Python')
dev2=developer("Ankita","Rane",70000,'Flask')
dev3=developer("Ramraj","Kumar",30000,'Django')
dev4=developer("Samir","Khan",40000,'Django')

mgr2=Manager('Aditya','Sharma',60000,[dev1,dev2,dev3])
print(emp1.fullname())
print(Employee.emp_count)
print(emp2.sal_increment())
print(emp3.email)

print(dev1.fullname())
print(Employee.emp_count)
print(dev2.sal_increment())

print(mgr1.printemp())
print(mgr2.printemp())
print(mgr2.addemp(dev4))
print(mgr2.printemp())
print(mgr1.removeemp(emp3))
print(mgr1.printemp())