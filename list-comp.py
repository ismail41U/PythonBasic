
numbers = [x for x in range(1, 21)]

even_numbers = [num for num in numbers if num % 2 == 0] # Filter even numbers
print("Even numbers:", even_numbers)

squared_even_numbers = [num ** 2 for num in even_numbers] # Square the even numbers
print("Squared even numbers:", squared_even_numbers)

print("------------------------------------------------------------------------------")

numbers = [x for x in range(1, 51) if x % 5 == 0]
print("Numbers divisible by 5 from 1 to 50:", numbers)

print("------------------------------------------------------------------------------")

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
long_words = [word for word in words if len(word) > 4]
print("Words longer than 4 characters:", long_words)

print("------------------------------------------------------------------------------")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

print("------------------------------------------------------------------------------")
# Create a list of tuples (number, square) for numbers from 1 to 10
number_square_tuples = [(num, num ** 2) for num in range(1, 11)]
print("Number and their squares:", number_square_tuples)

print("------------------------------------------------------------------------------")
# Create a list of characters from a given string, excluding vowels
input_string = "Python Programming"
characters = [char for char in input_string if char.lower() not in 'aeio']
print("Characters excluding vowels:", characters)

print("------------------------------------------------------------------------------")
# Create a list of factorials for numbers from 1 to 5
import math
factorials = [math.factorial(num) for num in range(1, 6)]
print("Factorials from 1 to 5:", factorials)

print("------------------------------------------------------------------------------")

years = [1990, 1995, 2000, 2005, 2010]
age = [2025 - year for year in years]
print("Ages for given birth years in 2025:", age)

print("------------------------------------------------------------------------------")

result = [x if x%2 == 0 else " odd" for x in range(1, 10)]
print("Result with conditional expressions:", result)

print("------------------------------------------------------------------------------")

# Create a nested list comprehension to generate a 3x3 matrix
nested_list = [[j for j in range(3)] for i in range(3)]
print("Nested list comprehension:", nested_list)

print("------------------------------------------------------------------------------")

# nested loops in list comprehension
print("------------------------------------------------------------------------------")
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print("Pairs of numbers from 1 to 3:", pairs)