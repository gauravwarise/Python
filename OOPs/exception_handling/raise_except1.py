a=input("Enter a: ")
b=input("enter b: ")
print(type(b))
if a.isdigit() and b.isdigit():
    x=int(a)
    y=int(b)
else:
    raise ValueError("Please enter numeric value")
if y==0:
    raise Exception("Please enter non zero value")
    
div=x/y
print(div)