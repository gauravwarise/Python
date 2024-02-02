# Write a program by creating an 'Employee' class having the following methods 
# and print the final salary. 1 - 'getInfo()' which takes the salary, number of 
# hours of work per day of employee asparameter2   -   'AddSal()'   which   adds   
# $10   to   salary   of   the   employee   if   it   is   less   than   $500.3 - 
# 'AddWork()' which adds $5 to salary of employee if the number of hours of work 
# perday is more than 6 hours

class Employee():
    def getInfo(self):
        self.salary=int(input("Enter salary: "))
        self.work_hours=int(input("Enter working hours per day: "))
        return self.salary,self.work_hours
    def AddSal(self):
        if self.salary<500.3:
            self.salary=self.salary+10
            return f"Salary after AddSal() : {self.salary}"
            # print(self.salary)
        else:
            pass
    def AddWork(self):
        if self.work_hours>6:
            self.salary=self.salary+5
            return f"Salary after AddWork() : {self.salary}"
            # print(self.work_hours)
        else:
            pass
ob1=Employee()
ob1.getInfo()
print(ob1.AddSal())
print(ob1.AddWork())
print("Final Salary: ", ob1.salary)