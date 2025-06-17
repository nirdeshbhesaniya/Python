friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("New Friend")  # Adding a new element to the end of the list
print(friends)

l1 = [1, 34,62, 2, 6, 11]

# l1.sort()
# l1.reverse()
# l1.insert(3, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(2)  # Remove the element at index 2 and return it
print(value)  # Print the value that was removed
l1.remove(34)  # Remove the first occurrence of 34 from the list
l1.clear()  # Clear the entire list
print(l1)