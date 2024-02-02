a =[1,2,3,4,5,6,7,8,9,10]
b =['a','b','c','d','e','f','g','h','i','j']
# output = [1,'a',2,'b',3,'c',....]
i = 0
temp = []
while(True):
    for j in range(len(a)):
        if i == j:
            temp.append(j)
        else:
            break
    for j in range(len(b)):
        if i == j:
            temp.append(j)
        else:
            break
    i+=1
    print(temp)

# temp = list(zip(a,b))
# print(temp)

# [1,'a',2,'b',3,'c']

# a = 3
# b = 4
# f = lambda a,b:a+b
# print(f(1,2))
# print(lambda:a,b:a+b)