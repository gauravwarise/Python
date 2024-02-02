num=int(input("Enter a number:"))
tot=0

while num:
    num=int(num/10)
    tot=tot+1
print("total digits are",tot)
