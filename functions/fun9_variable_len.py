def add(*x):
    print(x)
    print(type(x))
    c=0
    for i in x:
        c=c+i
    print("addition is",c)
add(20,50,26,35,93746)
add(20)