# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *
n=5
for i in range(n): #outer loop for rows
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()