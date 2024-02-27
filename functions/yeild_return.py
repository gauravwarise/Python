# Using return
def return_example():
    return 1
    print("This will not be executed")

result = return_example()
print(result)  # Output: 1

# Using yield
def yield_example():
    yield 1
    print("This will be executed")
    yield 2
    print("This will be executed")

generator = yield_example()
result = next(generator)
print(result)  # Output: 1

result = next(generator)
print(result)