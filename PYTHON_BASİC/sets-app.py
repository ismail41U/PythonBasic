
fruits = {"apple", "banana", "cherry"}
print(fruits)
print(type(fruits)) # Set type
print("Length of fruits set:", len(fruits)) # Length of the set
fruits.add("orange")
fruits.update(["mango", "grape"])
print("Fruits after adding orange:", fruits)
print(fruits)
fruits.remove("banana")
print(fruits)
print("Is apple in fruits?:", "banana" in fruits)
fruits.discard("grape") # Discarding an element
print(fruits)
fruits.pop() # Removing an arbitrary element
print("Fruits after popping an element:", fruits)

myList = [1, 2, 2, 3, 4, 4, 5]
mySet = set(myList) # Converting list to set to remove duplicates
print("Original List:", myList)
print("Set after removing duplicates:", mySet)
uniqueList = list(mySet) # Converting back to list
print("List after converting back from set:", uniqueList)