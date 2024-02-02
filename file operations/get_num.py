print("Search name by number: ")
snum=input("Enter number:")
fp=open('contact.txt','r')
clist=fp.readlines()
for x in clist:
    ltemp=x.split(":")
    if snum.isdigit()==True and len(snum)==10:
        if int(snum)==int(ltemp[1]):
            print("Match is found",ltemp)
        else:
            print("Match is not found")
    else:
        print("invalid number")
