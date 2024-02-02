class Error(Exception):
    pass

class IntIsTooSmall(Error):
    pass

class IntIsTooLarge(Error):
    pass

try:
    n = int(input("Enter number between 0 to 100: "))
    if int(n)<0:
        raise IntIsTooSmall
    elif int(n)>100:
        raise IntIsTooLarge
    else:
        print("Your number is {}".format(n))
        
except IntIsTooSmall:
    print("Entered number is less than 0.")
except IntIsTooLarge:
    print("Entered number is more than 100.")