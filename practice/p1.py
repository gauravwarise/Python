                                                        #                      1

                                                        #                 1           1

                                                        #           1          2         1

                                                        #       1       3           3       1

                                                        #   1         4         6        4      1
n=5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        C = 1
        print(C, ' ', sep='', end='')
        C = C * (i - j) // j
    print()
    # for j in range(i+1)


    # C = 1
    #   for j in range(1, i+1):
    #      print(C, ' ', sep='', end='')
    #      C = C * (i - j) // j
    #   print()