# mlist = ['a','b','c']

# mlist = list(filter(lambda x:x!='a', mlist))
# print(mlist)

# mlist = [1,2,3,4,5,1]
# mlist.sort(reverse=True)
# print(mlist)
# n = len(mlist)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if mlist[j]>mlist[j+1]:
#             mlist[j], mlist[j+1] = mlist[j+1], mlist[j]

# print(mlist)

mlist = [1,2,3,4,5,6,7,8,9,10]
n = len(mlist)
left = []
right = []
output = []
for i in range(n//2):
    left.append(mlist[i])
for i in range(n//2,n):
    right.append(mlist[i])
print(left)
print(right)
left.reverse()
right.reverse()
output.extend(right)
output.extend(left)
print(output)


# sum = 0
# for i in range(len(mlist)):
#     if i%2==0:
#         print(mlist[i], end=' ')
#         sum = sum+mlist[i]

# print(sum)  

# print(len(mlist)//2)
# for i in range(len(mlist)//2):
#     temp = mlist[i]
#     mlist[i] = mlist[len(mlist)-i-1]
#     mlist[len(mlist)-i-1] = temp

# print(mlist)