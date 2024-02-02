b=1
c=0
n=int(input("Enter hoe many terms in fibonacci series:"))
for i in range(1,n+1):
    if i==1:
        c=0
    elif i==2 or i==3:
        c=1
    else:
        a=b
        b=c
        c=a+b
    if i==n:
        print(c)
    else:
        print(c,end=" ")