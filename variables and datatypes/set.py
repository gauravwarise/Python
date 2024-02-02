myset={1,2,3,4,5}
print(myset)
print(type(myset))

myset1={1,2.4,"Hello",200,(1,2,3)}
print(myset1)

# to create set from list
myset2=set([1,2,3,7,10])
print(myset2)

myset3={}
print(type(myset3))

myset4=set()
print(type(myset4))

# to add single element/
myset5={1,2}
myset5.add(5)
print(myset5)

# to add multiple element/
myset5.update([6,7,8,9])
print(myset5)
 
# to add list and set/
myset5.update([12,13],(87,65))
print(myset5)

# to delete elements by using discard() and remove()/
myset5.discard(12)
print(myset5)

myset5.remove(13)
print(myset5)


print(myset5.pop())

# clear/
myset1.clear()
print(myset1)

