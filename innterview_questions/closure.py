numbers = []
def enter_number(x):
    numbers.append(x)
    print(numbers)
enter_number(3)
enter_number(5)
enter_number(36)

def enter_number_outer_function():
    numbers = []
    def enter_number_inner_function(x):
        numbers.append(x)
        print(numbers)
    return enter_number_inner_function

enter_numbers = enter_number_outer_function()
enter_numbers(3)
enter_numbers(5)
enter_numbers(36)