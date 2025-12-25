
numbers = [1,3,6,7,15,20,41,60,91]

for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")

print("--------------------------------------------------")
total = 0
for i in numbers:
    total += i
print(f"The total sum of the numbers is: {total}")

print("--------------------------------------------------"),

for i in numbers:
    if i % 2 == 1:
        print(f"The square of {i} is: {i ** 2}")

print("--------------------------------------------------")

factorial = 1
n = int(input("Enter a number to calculate its factorial: "))
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is: {factorial}")

print("--------------------------------------------------")

citys = ["New York", "Los Angeles", "Chicago", "Houston", "Las Vegas"]
for city in citys:
    if len(city) <= 8:
        print(f"{city} has 8 or fewer characters.")

print("--------------------------------------------------")

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 800},
    {"name": "Tablet", "price": 400},
    {"name": "Monitor", "price": 300},
    {"name": "Headphones", "price": 150}
]
for p in products:
    if p["price"] > 500:
        print(f"{p['name']} is expensive with a price of ${p['price']}.")

total_price = 0
for p in products:
    total_price += p["price"]
print(f"The total price of all products is: ${total_price}")
        

