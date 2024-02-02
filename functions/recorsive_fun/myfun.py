i=0
def myfun():
    global i 
    i=i+1
    print("my numbers are",i)
    myfun()
myfun()