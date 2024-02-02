class matrix():
    def __init__(self,r,c):
        self.r=r
        self.c=c
    def get_row(self):
        self.r=int(input("Enter number of rows of matrix: "))
    def get_col(self):
        self.c=int(input("Enter number of columns of matrix: "))
    def set_element(self):
        #------------------>Matrix first
        self.matrix1=[]
        for self.i in range(self.r):
            self.a=[]
            for self.j in range(self.c):
                print("Enter element on index",[self.i]," ",[self.j])
                self.a.append(int(input()))
            print()
            self.matrix1.append(self.a)
        print("First Matrix : ")
        # printing matrix 1
        for self.i in range(self.r):
            for self.j in range(self.c):
                print(self.matrix1[self.i][self.j],end=" ")
            print()
        #--------------->Matrix second
        self.matrix2=[]
        for self.i in range(self.r):
            self.a=[]
            for self.j in range(self.c):
                print("Enter element on index",[self.i]," ",[self.j])
                self.a.append(int(input()))
            print()
            self.matrix2.append(self.a)

        # printing matrix 1
        print("second Matrix : ")
        for self.i in range(self.r):
            for self.j in range(self.c):
                print(self.matrix2[self.i][self.j],end=" ")
            print()
        print()
    
    def mult_Matrix(self):
        self.multi_matrix=[]
        for self.k in range(self.r):
            for self.i in range(self.r):
                self.temp_matrix=[]
                self.add=0
                for self.j in range(self.c):
                    self.a=self.matrix1[self.i][self.j]*self.matrix2[self.j][self.i]
                    self.add=self.add+self.a
                    self.temp_matrix.append(self.add)
                self.multi_matrix.append(self.temp_matrix)
                
        print(self.multi_matrix)


ob1=matrix(2,2)
ob1.get_row()
ob1.get_col()
ob1.set_element()
ob1.mult_Matrix()
