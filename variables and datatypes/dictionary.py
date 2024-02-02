from xml.dom.minidom import Element


my_dict={1:'apple',2:'mango'}
print(my_dict)

my_dict1={'name':'raj',1:[1,2,3,4]}
print(my_dict)

# add element by using dict()
my_dict=dict({8:'apple',5:'mango'})
print(my_dict)

# from sequence having each item in pair
my_dict=dict([(1,'car'),(2,'bike')])
print(my_dict)

# access element from dictionary/
print(my_dict[2])

print(my_dict1['name'])

index1=list(my_dict1.values())
print(index1[1])

print(my_dict.get('name'))
# print(my_dict['name'])

# add element in dictionary/
my_dict[3]='cycle'

my_dict[3]='train'
print(my_dict)

# remove Element from dictionary
square={1:1,2:4,3:9,4:16,5:25,6:36}
print(square.pop(4))
print(square) 

print(square.popitem())
print(square)

my_dict.clear()
print(my_dict)

# del my_dict1
# print(my_dict1)