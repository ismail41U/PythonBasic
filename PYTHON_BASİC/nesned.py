
# encapsulation with nested functions
def outer(num1):
    print("Outer function")
    
    def inner(outer):
        print("Inner function")
        return num1 + 5
    num2 = inner(num1)
    print(num1, num2)
    
outer(10)
# inner(5)  # This will raise an error because inner is not accessible here
print("------------------------------------------------")

def factorial(n):
    """Calculate factorial of a number using nested function."""
    def inner_factorial(x):
        if x == 0 or x == 1:
            return 1
        else:
            return x * inner_factorial(x - 1)
    
    return inner_factorial(n)

print("Factorial of 5 is:", factorial(5))
print("Factorial of 0 is:", factorial(0))   
print("------------------------------------------------")

def power(base, exponent):
    """Calculate power using nested function."""
    def inner_power(b, e):
        result = 1
        for _ in range(e):
            result *= b
        return result
    
    return inner_power(base, exponent)

print("2 raised to the power 3 is:", power(2, 3))
print("5 raised to the power 0 is:", power(5, 0))
print("------------------------------------------------")

