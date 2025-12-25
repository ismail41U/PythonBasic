## Lambda, Map, and Filter in Python

def square(num): return num ** 2
numbers = list(range(1, 10))
result = list(map(square, numbers))
print("Squares using named function:", result)

print("------------------------------------------------------------------------------")

# Using lambda function with map

result_lambda = list(map(lambda x: x ** 2, numbers))
print("Squares using lambda function:", result_lambda)

print("------------------------------------------------------------------------------")

# Using filter with named function
def is_even(num): return num % 2 == 0
even_numbers = list(filter(is_even, numbers))
print("Even numbers using named function:", even_numbers)

print("------------------------------------------------------------------------------")
# Using filter with lambda function

even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda function:", even_numbers_lambda)

print("------------------------------------------------------------------------------")

country = ["Turkey", "Tunus", "France", "Italy", "Spain", "Iraq", "Greece", "Tailand"]
countries_starting_with = list(filter(lambda x: x.startswith('T'), country))
print("Countries starting with 'T':", countries_starting_with)

print("------------------------------------------------------------------------------")

countries_endwith_with = list(filter(lambda x: x.endswith('y'), countries_starting_with))
print("Countries ending with 'y':", countries_endwith_with)

print("------------------------------------------------------------------------------")

# Combining map and filter

squared_even_numbers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print("Squared even numbers using map and filter:", squared_even_numbers)

print("------------------------------------------------------------------------------")
# Using lambda with reduce
from functools import reduce
product_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Product of numbers from 1 to 9 using reduce:", product_of_numbers)

print("------------------------------------------------------------------------------")

# Using lambda with sorted
unsorted_numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(unsorted_numbers, key=lambda x: x)
print("Sorted numbers using lambda:", sorted_numbers)

print("------------------------------------------------------------------------------")

# Using lambda with max and min
max_number = max(numbers, key=lambda x: x)
min_number = min(numbers, key=lambda x: x)
print("Max number using lambda:", max_number)
print("Min number using lambda:", min_number)

print("------------------------------------------------------------------------------")

# Using lambda with list comprehension
squared_numbers_comp = [ (lambda x: x ** 2)(x) for x in numbers ]
print("Squared numbers using lambda in list comprehension:", squared_numbers_comp)

print("------------------------------------------------------------------------------")
# Using lambda with conditional expressions
conditional_result = [ (lambda x: x if x % 2 == 0 else " odd")(x) for x in range(1, 10) ]
print("Conditional result using lambda:", conditional_result)

print("------------------------------------------------------------------------------")
# Using lambda with nested functions
def apply_function(func, value):
    return func(value)  
result_nested = apply_function(lambda x: x ** 3, 3)
print("Result of nested lambda function (cube of 3):", result_nested)

print("------------------------------------------------------------------------------")

# Using lambda with multiple arguments
add = lambda x, y: x + y
sum_result = add(5, 7)  
print("Sum using lambda with multiple arguments:", sum_result)

print("------------------------------------------------------------------------------")

# Using lambda with default arguments
multiply = lambda x, y=2: x * y
multiply_result = multiply(5)   
print("Multiply using lambda with default argument:", multiply_result)

print("------------------------------------------------------------------------------")
# Using lambda with variable-length arguments
sum_all = lambda *args: sum(args)
total_sum = sum_all(1, 2, 3, 4, 5)
print("Total sum using lambda with variable-length arguments:", total_sum)

print("------------------------------------------------------------------------------")

# Using lambda with dictionaries
dict_items = {'a': 1, 'b': 2, 'c': 3}
sorted_dict = dict(sorted(dict_items.items(), key=lambda item: item[1]))
print("Sorted dictionary using lambda:", sorted_dict)

print("------------------------------------------------------------------------------")
# Using lambda with list of tuples
tuples_list = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[0])
print("Sorted list of tuples using lambda:", sorted_tuples)

print("------------------------------------------------------------------------------")
# Using lambda with sets
numbers_set = {5, 2, 9, 1, 5, 6}
sorted_set = sorted(numbers_set, key=lambda x: x)
print("Sorted set using lambda:", sorted_set)

print("------------------------------------------------------------------------------")
# Using lambda with strings 

strings = ["apple", "banana", "cherry", "date"]
sorted_strings = sorted(strings, key=lambda x: len(x))
print("Sorted strings by length using lambda:", sorted_strings)

print("------------------------------------------------------------------------------")

# Using lambda with recursion
factorial = (lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
factorial_result = factorial(6)
print("Factorial using recursive lambda:", factorial_result)

