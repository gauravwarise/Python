# user define custom Exception
class error(Exception):
    pass
class valueTooSmallError(error):
    pass
class valueTooLargeError(error):
    pass
num=20
while True:
    try:
        unum=int(input("Enter a number: "))
        if unum<num:
            raise valueTooSmallError
        elif unum>num:
            raise valueTooLargeError
        break
    except valueTooSmallError:
        print("This value is too small, Please try again")
        print()
    except valueTooLargeError:
        print("This value is too large, Please try again")
        print()
print("Congrats!!!>>> Your guess is correct.")

        