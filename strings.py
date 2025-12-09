
name = "Kaan"
surname = "Sütdonduran"
age = "17"

greeting = "Hello, my name is "+ name + " " + surname + " and I am "+ age +" years old"
greeting_one = ("Hello, my name is {} {} and I am {} years old").format(name, surname, age)
greeting_two = f"Hello, my name is {name} {surname} and I am {age} years old"
print(greeting)
print(greeting_one)
print(greeting_two)

"""This is a multiline string.It can span multiple lines."""

print(greeting[0])
print(greeting[0:5])  # Slicing
print(greeting[-3:])   # Slicing from the end
print(greeting[0:20:2])  # Slicing with step
print(len(greeting))  # Length of the string
print(greeting[-1])


result = 200 / 700
print("The result is {}".format(result))   # Basic formatting
print("The result is {:.2f}".format(result))  # Formatting float to 2 decimal places
print("The result is {:7.4}".format(result))  # Formatting float with width and precision

website = "www.example.com"
course = "Welcome to the Python Programming course"

print(f"Length of the string : ",len(course))  # Length of the string
print(course[15:21])  # Length with slicing
print(website.count("w"))  # Count occurrences of 'w'
print(course.count("o", 0, 20))  # Count occurrences of 'o' in a substring
print(website.startswith("www"))  # Check if starts with 'www'
print(website.endswith("com"))  # Check if ends with 'com'
print(course.find("Python"))  # Find substring
print(course.find("Java"))  # Find substring that doesn't exist
print(course.index("Python"))  # Index of substring
#print(course.index("Java"))  # This would raise an error
print(course.isalpha())  # Check if all characters are alphabetic
print("Welcome".isalpha())  # Check if all characters are alphabetic
print("12345".isdigit())  # Check if all characters are digits
print("Welcome to the Python Programming course".upper())  # Convert to uppercase
print("Welcome to the Python Programming course".lower())  # Convert to lowercase
print("Welcome to the Python Programming course".capitalize())  # Capitalize first letter
print("Welcome to the Python".title())  # Title case
print("Python Programming".replace("Python", "C++"))  # Replace substring
print("     Welcome to the Python Programming course     ".strip())  # Remove leading and trailing whitespace
print("Welcome to the Python Programming course".split())  # Split into list of words
print("www.example.com".split("."))  # Split by dot