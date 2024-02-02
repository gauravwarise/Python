try:
    a=4
    b=5
    print(a+b)
    print("Try block is executed.")
except Exception as e:
    print("Error occured: ",e)
finally:
    print("Finally block is executed.")