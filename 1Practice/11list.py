def swaplist(newlist):
    # size = len(newlist)

    temp = newlist[0]
    newlist[0] = newlist[-1]
    newlist[-1] = temp
    return newlist

newlist = [4,3,5,0,6]
print(swaplist(newlist))
