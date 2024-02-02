n1=int(input("Enter numerator: "))
n2=int(input("Enter denominator: "))
# div=n1/n2
# print(div)
try:
    div=n1/n2
    print(div)
except:
    print("Can not divisible by zero,please enter valid value")