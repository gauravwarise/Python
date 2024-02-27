arr = [1,2,3]
count = 0
element = None
for e in arr:
    print(count)
    if count==0:
        element=e
    count +=(1 if e==element else -1)

print(count, element)

