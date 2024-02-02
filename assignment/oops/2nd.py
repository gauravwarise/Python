from math import sqrt
try:
    print(5/0)
except ZeroDivisionError as e:
    print("zero division error:",e)

try:
    print(5+"6")
except TypeError as e:
    print("type error:",e)

try:
    print(sqrt(-16))
except ValueError as e:
    print("value error:",e)

try:
    print()
except NameError as e:
    print("name error:",e)