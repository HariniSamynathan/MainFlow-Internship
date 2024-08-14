# Creating a set
my_set = {1, 2, 3, 4, 5}
print("\nInitial Set:", my_set)

# Adding elements to the set
my_set.add(6)  # Add a new element
print("Set after adding an element:", my_set)

# Removing elements from the set
my_set.discard(3)  # Remove by value (doesn't raise an error if not found)
removed_set_element = my_set.pop()  # Remove an arbitrary element
print("Set after removing an element:", my_set)
print("Removed element from set:", removed_set_element)