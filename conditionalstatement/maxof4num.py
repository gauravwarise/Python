a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))
max=None
# if a>b:
#     max==a
#     if max<c:
#         max==c
#         if max<d:
#             print(max, "is max number")
# else:
#     max==b
#     if max<c:
#         max==c
#         if max<d:
            # print(max, "is max number")

if a>b:
    if a>c:
        if a>d:
            print(a, " is greater.")
elif b>c:
    if b>d:
        print(b," is greater.")
elif c>d:
    print(c," is greater.")
else:
    print(d, " is greater.")