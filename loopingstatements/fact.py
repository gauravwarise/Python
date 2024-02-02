from re import I


num=int(input("Enter a number:"))
fact=1

# for i in range(1,num+1):
#     fact=fact*i
# print("Factorial of number",num,"=", fact)

i=1
while i<=num:
    fact=fact*i
    i+=1
print("Factorial of number",num,"=", fact)