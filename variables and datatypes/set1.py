a={1,2,3,4,5}
b={4,5,6,7,8,9}

# union/
c=a|b
# print(c)
print(a.union(b))
print(type(c))

# intersection
# print(a&b)
print(a.intersection(b))

# difference/
print(a-b)
print(b-a)