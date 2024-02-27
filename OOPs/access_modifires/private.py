class Info():
    #private numbers
    __name=None
    __rollno=None
    __location=None
    

    #constructor
    def __init__(self,name,rollno,location):
        self.name=name
        self.rollno=rollno
        self.location=location
    
    # private method
    def __display(self):
        # access private attributes
        print("Name: ", self.name)
        print("Roll Number: ", self.rollno)
        print("Name: ", self.name)
    # public method
    def displayinfo(self):
        self.__display()
obj1=Info("gaurav",101,"Thane")
obj1.displayinfo() 