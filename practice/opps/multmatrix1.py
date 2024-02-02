r=int(input("Enter number of rows of matrix: "))
c=int(input("Enter number of columns of matrix: "))
matrix1=[]
for i in range(r):
    a=[]
    for j in range(c):
        print("Enter element on index",[i]," ",[j])
        a.append(int(input()))
    print()
    matrix1.append(a)
print("First Matrix : ")
    # printing matrix 1
for i in range(r):
    for j in range(c):
        print(matrix1[i][j],end=" ")
    print()
#--------------->Matrix second
matrix2=[]
for i in range(r):
    a=[]
    for j in range(c):
        print("Enter element on index",[i]," ",[j])
        a.append(int(input()))
    print()
    matrix2.append(a)

        # printing matrix 1
print("second Matrix : ")
for i in range(r):
    for j in range(c):
        print(matrix2[i][j],end=" ")
    print()
print()
    
multi_matrix=[]
result=0
for i in range(r):
    for j in range(c):
        temp_matrix=[]
        for k in range(c):
            result = result + matrix1[i][k] * matrix2[k][j]
        temp_matrix.append(result)
    multi_matrix.append(temp_matrix)
print(multi_matrix)
# for k in range(r):
#     for i in range(r):
        
#         add=0
#         for j in range(c):
#             a=matrix1[k][i]*matrix2[k][j]
#             add=add+a
#             temp_matrix.append(add)
        
# print(multi_matrix)



