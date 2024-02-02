try:
    n1=int(input("Enter Numerator: "))
    n2=int(input("Enter denominator: "))

    div=n1/n2
except Exception as e:
    print("Error: ",e)
# except ValueError:
#     print("Enter valid number")
else:
    print("Division is ",div)
finally:
    print("In Finally") #Finally should be at the end 

