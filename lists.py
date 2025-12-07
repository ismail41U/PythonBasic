
list_one = [1, 2, 3, 4, 5]
list_two = ["one",5 ,8.6, True]
combined_list = list_one + list_two
print(list_one)
print(list_two)
print("Length of List One:", len(list_one))
print("Combined List:", combined_list)

print(combined_list[2])
print(combined_list[-1])

new_list = [list_one,list_two]
print("New List:", new_list)
print("First element of the second list in New List:", new_list[0][0])
print("First element of the second list in New List:", new_list[1][2])
list_one.append(6)
print("List One after appending 6:", list_one)
print("Combined List after appending 6 to List One:", combined_list)

cars = ["BMW", "Audi", "Toyota", "Honda"]
print("Original Cars List:", cars)

print(len(cars))# Output the length of the list
print(cars[0]) # Access the first element
print(cars[-1]) # Access the last element
## print(cars.replace("BMW", "Mercedes")) ^# This will raise an AttributeError since lists do not have a replace method
cars[0] = "Mercedes" # Modify the second element
print("Cars List after modification:", cars)
print("Index of 'Toyota':", cars.index("Toyota")) # Find the index of an element