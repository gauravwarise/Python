a=float(input("Enter sub1 marks:"))
b=float(input("Enter sub2 marks:"))
c=float(input("Enter sub3 marks:"))
d=float(input("Enter sub4 marks:"))

total=float(a+b+c+d)
avg=total/4

if avg>75:
    print("A+")
elif avg<74 and avg>60:
    print("A")
elif avg<59 and avg>50:
    print("B")
elif avg<49 and avg>40:
    print("C")

