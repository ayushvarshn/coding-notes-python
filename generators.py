# Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. 
# Generator objects are used either 1. calling the next method of the generator object 2. using the generator object in a “for in” loop.

def fib(limit): 
    a, b = 0, 1
    while a < limit: 
        yield a 
        a, b = b, a + b 

# In Loop
for i in fib(5):  
    print(i)

# Using next
f = fib(5)
print(next(f))
print(next(f))
print(next(f))
