menu=[100,12.5,'Rice',[1,2,50],'Wheat',500,10,20]
print(menu)
# append
menu.append(56)
print(menu)

# insert
menu.insert(2,111)
print(menu)

# extend
menu.extend([23,'rahul',886])
print(menu)

# remove
menu.remove(23)
print(menu)

# pop
menu.pop(1)
print(menu)

# slice
print(menu[2:5])

# reverse
menu.reverse()
print(menu)

# length
print(len(menu))

list1=['a',['bb','cc'],1,5.9,[2,4]]
list1[1].insert(0,'xx')
print(list1)