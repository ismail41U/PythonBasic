def exponent(power):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result ** power
        return wrapper
    return decorator
@exponent(2)
def add(a, b):
    return a + b    
@exponent(3)
def multiply(a, b):
    return a * b

# Example usage:
print(add(2, 3))       # Output: 25, because (2 + 3)^2 = 25
print(multiply(2, 3))  # Output: 216, because (2 * 3)^3 = 216   
@exponent(2)
def square(n):
    return n    
print(square(4))       # Output: 16, because (4)^2 = 16

print("--------------------------------------------------------")

import math
import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)  # Simulating a delay
        func(*args, **kwargs)
        finish = time.time()
        print("Time taken to execute the function: ", finish - start)
        
    return wrapper

@calculate_time
def exponent(a, b):

    print(math.pow(a, b))

@calculate_time
def factorial(n):

    print(math.factorial(n))

exponent(2, 3)
factorial(5)
