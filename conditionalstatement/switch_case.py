import time

def case1():
    return "This is case 1"

def case2():
    return  "This is case 2"

def case3():
    return  "This is case 3"



switch_case = {
    1:case1,
    2:case2,
    3:case3
}

def switch(argument):
    return switch_case.get(argument, lambda:"Invalid case")()
start_time = time.time()
print(switch(3))
print(switch(1))


end_time = time.time()

print(end_time-start_time)