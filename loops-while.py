
numbers = [1, 5, 11, 13, 16, 18, 19]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print("--------------------------------------------------")

start = int(input("Starting number of the range: "))
end = int(input("Ending number of the range: "))

i = start
while i <= end:
    if i % 2 == 1:
        print(f"{i} is an odd number.")
    i += 1

print("--------------------------------------------------")

i = 101

while range(1,101):
    i -= 1
    print(i)
    if i == 0:
        break

print("--------------------------------------------------")

numbers = [] 

i = 0
while i < 5:
    int_num = int(input("Enter a number to add to the list: "))
    numbers.append(int_num)
    i += 1

    numbers.sort()
print(f"The numbers you entered are: {numbers}")

print("-----------------------------------------------------")##

product = []
piece = int(input("Enter number of products : "))
i = 0
while (i < piece) :
    name = input("Product Name : ")
    price = (input("Product Price : "))
    product.append({
        "Product Name ": name,
        "Product Price ": price
    })

    i += 1
for x in product:
    print(f"Product Name: {x['Product Name ']} / Product Price: {x['Product Price ']}")
    







