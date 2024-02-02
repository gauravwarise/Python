from audioop import reverse
from operator import length_hint
from os import remove


mylist=[1,2,3,'ITVedant','This is full stack']
# print(type(mylist))

# uppend
mylist.append(4)
mylist.append(5)
for i in range(7,9):
      mylist.append(i)

# extend
mylist.extend([34,3,43,54])
print('endent mylist ----->',mylist)
# insert
mylist.insert(3,100)

# remove
mylist.remove(100)

# pop
mylist.pop(4)
print("pop: ",mylist)

# slice
# print(mylist[2:4]) or
sublist=mylist[2:4]
print(sublist)
print(mylist[:4])
print(mylist[4:])

# reverse
mylist.reverse()

# length
print(len(mylist))

print(mylist)

