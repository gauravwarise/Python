rows=int(input("Enter rows: "))
col=int(input("Enter column: "))

matrix=[]
for i in range(rows):
    tempmatrix=[]
    for j in range(col):
        print("Enter elements on index",i," ",j," : ")
        tempmatrix.append(int(input()))
    matrix.append(tempmatrix)

print(matrix)

for i in range(rows):
    for j in range(col):
     print(matrix[i][j],end=" ")
    print()