# zip function
# It is usd to combine two list together ,
# no matter whether list is balanced or imbalanced

list1=[1,2,3,4,5,6,7]
list2=["a","b","c","d"]
mydict = zip(list2, list1)
print(mydict)
for i,j in mydict:
    print(i,j)
# for i,j in zip(list1,list2):
#     print(i,j)