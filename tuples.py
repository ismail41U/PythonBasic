
list_one = [1, 2, 2, 3, 4, 5]
tuple_one = (8,"E", 3.14, False)
print("List One:", list_one)
print("Tuple One:", tuple_one)
print("Length of Tuple One:", len(tuple_one))   
print("Second element of Tuple One:", tuple_one[1])# Access the second element
print("Last element of Tuple One:", tuple_one[2])# Access the last element
list_one[1] = 10# Modify the second element of the list
print("List One after modification:", list_one)
##tuple_one[1] = "A" # This will raise a TypeError since tuples are immutable
nested_tuple = (tuple_one, tuple(list_one))# Convert list_one to a tuple for nesting
print("Nested Tuple:", nested_tuple)
print("First element of the second tuple in Nested Tuple:", nested_tuple[1][0])# Access first element of the second tuple
list_one.append(6)# Append an element to the list
print("List One after appending 6:", list_one)
print("Tuple One remains unchanged after modifying List One:", tuple_one)
print("Index of 3.14 in Tuple One:", tuple_one.index(3.14))# Find the index of an element in the tuple
print("Number of times 2 appears in List One:", list_one.count(2))# Count occurrences of an element in the list
result = 3 in tuple_one## Check membership in the tuple
print("Is 3 in Tuple One?:", result)
result = 10 in list_one ## Check membership in the list
print("Is 10 in List One?:", result)
sliced_tuple = tuple_one[1:3]# Slicing the tuple
print("Sliced Tuple (elements from index 1 to 2):", sliced_tuple)
reversed_tuple = tuple_one[::-1]## Reversing the tuple using slicing
print("Reversed Tuple using slicing:", reversed_tuple)
single_element_tuple = (42,)## Creating a single-element tuple
print("Single Element Tuple:", single_element_tuple)
empty_tuple = ()## Creating an empty tuple
print("Empty Tuple:", empty_tuple)   
