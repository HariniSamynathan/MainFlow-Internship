# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

# Adding elements to the list
my_list.append(6)  # Add to the end
my_list.insert(0, 0)  # Add at index 0
print("List after adding elements:", my_list)

# Removing elements from the list
my_list.remove(3)  # Remove by value
removed_element = my_list.pop()  # Remove the last element
print("List after removing elements:", my_list)
print("Removed element:", removed_element)

# Modifying elements in the list
my_list[1] = 10  # Change the element at index 1
print("List after modifying an element:", my_list)