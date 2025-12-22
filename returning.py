
def power(number):

    def inner(exponent):
        return number ** exponent
    return inner

square = power(4)
print(square(2))  # Output: 16
cube = power(3)
print(cube(3))    # Output: 27

print("------------------------------------------------")

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply 
double = make_multiplier(2)
print(double(5))  # Output: 10
triple = make_multiplier(3)
print(triple(5))  # Output: 15

print("------------------------------------------------")
def greeting(message):
    def greet(name):
        return f"{message}, {name}!"
    return greet
hello = greeting("Hello")
print(hello("Alice"))  # Output: Hello, Alice!
good_morning = greeting("Good morning")
print(good_morning("Bob"))  # Output: Good morning, Bob!

print("------------------------------------------------")

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

count1 = counter()
print(count1())  # Output: 1
print(count1())  # Output: 2
count2 = counter()
print(count2())  # Output: 1
print(count1())  # Output: 3

print("------------------------------------------------")

def logger(prefix):
    def log(message):
        print(f"{prefix}: {message}")
    return log  
info_logger = logger("INFO")
info_logger("This is an informational message.")  # Output: INFO: This is an informational message.
error_logger = logger("ERROR")
error_logger("This is an error message.")  # Output: ERROR: This is an error message.
print("------------------------------------------------")

