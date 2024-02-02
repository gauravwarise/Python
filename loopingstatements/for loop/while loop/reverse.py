# palindromm

x=int(input("Enter a number:"))
rev=0
orig=x
while x>0:
    rem=x%10
    rev=rem+(rev*10)
    x=int(x/10)
print(rev, "reverse number is")


if orig==rev:
    print("Number is equal to reverse")
else:
    print("Number is not equal to reverse")
