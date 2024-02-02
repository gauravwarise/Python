list=["rahul",2746274645,"21/5/2001","thane"]
for i in list:
    print(i)

print(type(list))
# add elements
list.append("jadhav")
list.insert(2,"developer")
list.extend(["cricket","reading books"])
print(list)

# slicing
print(list[1:3])
print(list[1:])
print(list[:3])
print(list[:])

list.reverse()
print(list)

print(len(list))

list.pop(1)
print(list)
