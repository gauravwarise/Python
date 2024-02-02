def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
n=int(input("Enter a Number"))
if n<=0:
    print("Factorial does not exist")
else:
    print("Factorial of number is",fact(n))