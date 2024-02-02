# reduce function
# for this , it is meccessary to import functools
# syntax:reduce(function_name,collection)

import functools
list1=[1,2,3,4,5]
# use reduce function to find sum element from list
print("The sum of list of elements is", end=" ")
print(functools.reduce(lambda a,b:a+b,list1))
# use reduce function to find max element from list
print("The max  of list of elements is", end=" ")
print(functools.reduce(lambda a,b:a if a>b else b,list1))