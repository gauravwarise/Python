l = [0,-10,1,3,-20]


for i in range(len(l)):
    for j in range(1,len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

print(l[-1]+1)

print(l)