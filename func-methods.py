
# Demonstration of for loops with different ranges and conditions
for i in range(10): # Numbered from 0 to 9
    if i % 3 == 0:
        print(i)
print("1 ")

for i in range(10, 100, 10): # Numbered from 10 to 90 with step of 10
    print(i)
print("------------------------------------------------------------------------------")

# enumerate function to get index and value
name = "Ela"
index = 0
for letter in name:
    print(f"Index: {index}, Value: {letter}")
    index += 1

print("Enumerate function output : ") 

index = 0
for index, letter in enumerate(name):
    print(f"Index: {index}, Value: {letter}")

print("------------------------------------------------------------------------------")

# zip function to combine two lists

names = ["Kaan", "Ela", "Ismail"]
ages = [17, 7, 47]

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

names.append("Ahmet")
ages.append(25)

print("After appending new values : ")
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

names = ["Kaan", "Ela", "Ismail"]
phones = ["555-1234", "555-5678", "555-8765"]
citys = ["Istanbul", "Istanbul", "Kocaeli"]

for name, phone, city in zip(names, phones, citys):
    print(f"Name: {name}, Phone: {phone}, City: {city}")

print("------------------------------------------------------------------------------")


    


