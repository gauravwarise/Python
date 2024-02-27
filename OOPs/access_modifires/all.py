class calc():
    var1=None
    __var2=None
    _var3=None

    def __init__(self,var1,__var2,_var3):
        self.var1=var1
        self.__var2=__var2
        self._var3=_var3    

    # public method
    def displaypub(self):
        print("Public data: ",self.var1)
    # private method
    def __displaypri(self):
        print("Private data: ",self.__var2)
    # protected method
    def _displayprotected(self):
        print("Protected data: ",self._var3)
    
    def accesspri(self):
        self.__displaypri()


class subcalc(calc):
    # constructor
    def __init__(self,var1,var2,var3):
        calc.__init__(self,var1,var2,var3)
    def accessprotected(self):
        self._displayprotected()

    # def accessprivate(self):
    #     self.__displaypri()

ob1=subcalc("abc",2,"xyz")
ob1.displaypub()
ob1.accesspri()
ob1.accessprotected()
# ob1.accessprivate()

        