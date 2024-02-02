try:
    n1=int(input("Enter numerator: "))
    n2=int(input("Enter denominator: "))
# div=n1/n2
# print(div)

    div=n1/n2
    print(div)
except ZeroDivisionError:
    print("Can not divisible by zero,please enter valid value")
except ValueError:
    print("Enter valid number")
finally:
    print("In Finally block")