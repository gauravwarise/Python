def funct1():
    return "hello func 1 is here"
def funct2():
    return "hello func 2 is here"
def funct3():
    return "hello func 3 is here"

switch_case = {
    1:funct1,
    2:funct2,
    3:funct3,
}
# switch_case[5]
# switch_case.get(5)

def switch(arg):
    return switch_case.get(arg, lambda:"Invalid argument")()

print(switch(1))