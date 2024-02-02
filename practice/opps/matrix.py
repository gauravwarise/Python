r=int(input("Enter number of rows: "))
c=int(input("Enter number of colunm: "))
matrix1=[]
for i in range(r):
    a=[]
    for j in range(c):
        print("Enter number in matrix on index: ",i," ",j," :",end=" ")
        a.append(int(input()))
    print()
    matrix1.append(a)

print("Matrix 1: ")
for i in range(r):
    for j in range(c):
        print(matrix1[i][j],end=" ")
    print()


matrix2=[]
for i in range(r):
    a=[]
    for j in range(c):
        print("Enter number in matrix on index: ",i," ",j," :",end=" ")
        a.append(int(input()))
    print()
    matrix2.append(a)

print("Matrix 2: ")
for i in range(r):
    for j in range(c):
        print(matrix2[i][j],end=" ")
    print()