print("Search contact by name")
sname=input("Enter name: ")
stemp=sname.capitalize()
fp=open('contact.txt','r')
clist=fp.readlines()
for x in clist:
    ltemp=x.split(":")
    if ltemp[0].capitalize()==stemp:
        print("Match is found",x)
    else:
        print("Match is not found")
        