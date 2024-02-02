from ast import Num


num=int(input("Enter a number:"))
sum=0
while num != 0:
    rem=num%10
    squ=rem*rem
    sum=int(sum+squ)
    num=num/10
print(" sum is :", sum) 