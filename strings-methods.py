
message = "Hello, there! Welcome to string methods in Python."

print("Original Message:", message)
print("Capitalized:", message.capitalize())
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())
print("Replaced 'string' with 'text':", message.replace("string", "text"))
print("Stripped Message:", message.strip)
print("Split Message:", message.split(" "))
print("Number of characters in the original message:", len(message))
print("Does the message start with 'Hello'? :", message.startswith("Hello"))
print("Does the message end with 'Python.'? :", message.endswith("Python."))
print("Index of 'Welcome':", message.find("Welcome"))
print("Is the message alphabetic?:", message.isalpha())
print("Is 'Hello123' alphanumeric?:", "Hello123".isalnum())