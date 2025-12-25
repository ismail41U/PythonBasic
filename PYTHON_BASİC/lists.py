
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
print(cars[-2]) # Access the second last element
print("Sorted Cars List:", sorted(cars)) # Output a sorted version of the list without modifying the original   
print("Original Cars List remains unchanged:", cars) 
cars.sort() # Sort the list in place
print("Cars List after in-place sort:", cars) 
print("Index of 'Toyota' in Cars List:", cars.index("Toyota")) # Find the index of an element  
print("Number of times 'Audi' appears in Cars List:", cars.count("Audi")) # Count occurrences of an element  
cars.append("Ford") # Add an element to the end of the list
cars.append("Chevrolet") # Add another element to the end of the list
cars.append("Renault") # Add another element to the end of the list
cars.remove("Honda") # Remove an element from the list
print("Cars List after removing 'Honda':", cars)
cars.pop() # Remove and return the last element
print("Cars List after popping the last element:", cars)
del cars[3] # Delete the element at index 3
print("Cars List after deleting element at index 3:", cars)
cars.insert(1, "Volkswagen") # Insert an element at a specific position
print("Cars List after inserting 'Volkswagen' at index 1:", cars)
cars.reverse() # Reverse the list in place
print("Cars List after reversing:", cars)
print(cars[::-1]) # Slicing the list to get a reversed version
print(cars[0:3]) # Slicing the list from index 1 to 3

student_one = ["Alice", 20, [90, 85, 88]]
student_two = ["Bob", 22, [78, 82, 80]]
student_three = ["Charlie", 19, [65, 92, 96]]
students = [student_one, student_two, student_three]
print("Students List:", students)
print("Name of Student Two:", students[1][0])
print("Age of Student Three:", students[2][1]) 
print("Scores of Student One:", students[0][2])
print("First score of Student Two:", students[1][2][0])


