'''
Generator:
    Generator are iterators which can executes only once
    Generator uses "yield" keyword
    Every generator is an iterator

Iterator:
    iterators which can executes many times
    Iterator uses iter() and next() functions
    Every iterator is not a generator

'''

# Generator

def sqr(n):
    for i in range(1,n+1):
        yield i**i

a = sqr(3)
print(next(a))
print(next(a))
print(next(a))

# Iterator
iter_list = iter(['a', 'b', 'c'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))