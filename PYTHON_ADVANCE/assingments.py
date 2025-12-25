
x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 2 

user_one = int(input("Enter a user_one : "))
user_two = int(input("Enter a user_two : "))

result = (user_one * user_two) - (x + y + z)
print("The result is :", result)

result = y // x 
print("The result of y // z is :", result)

result = (x + y + z) % 3
print("The result of (x + y + z) % 3 is :", result)

result = y ** x
print("The result of y ** x is :", result)

x, *y, z = numbers
print("x :", x)
print("*y total :", y[0] + y[1] + y[2])
print("z :", z ** 3)