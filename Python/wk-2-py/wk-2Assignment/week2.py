"""
This is the answer to my week 2 assignment. 
* Create an empty list called my_list.
* Append the following elements to my_list: 10, 20, 30, 40.
* Insert the value 15 at the second position in the list.
* Extend my_list with another list: [50, 60, 70].
* Remove the last element from my_list.
* Sort my_list in ascending order.
* Find and print the index of the value 30 in my_list.
"""
# Below is the code that accomplishes the tasks outlined in the assignment:

# Create an empty list called my_list
my_list = []
print("Initial empty list:", my_list)
print()

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
print("After appending 10:", my_list)
print()
my_list.append(20)
print("After appending 20:", my_list)
print()
my_list.append(30)
print("After appending 30:", my_list)
print()
my_list.append(40)
print("After appending 40:", my_list)
print()

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)
print()

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)
print()

# Remove the last element from my_list
removed_element = my_list.pop()
print(f"After removing the last element ({removed_element}):", my_list)
print()

# Sort my_list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)
print()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of the value 30 in my_list:", index_of_30)
print()

# That concludes the assignment tasks.
print("Final state of my_list:", my_list)

