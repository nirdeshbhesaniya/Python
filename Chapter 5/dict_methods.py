marks = {
    "Nirdesh":95,
    "Harshil":85,
    "Charmi":90,
    0:"Hepin"
}

print(marks.items()) # Returns a view object that displays a list of a dictionary's key-value tuple pairs
print(marks.keys()) # Returns all keys in the dictionary
print(marks.values()) # Returns all values in the dictionary
marks["Hepin"] = 100 # Adding a new key-value pair
print(marks) # Updated dictionary with new key-value pair
print(marks.get("Nirdesh")) # Accessing value using get method
marks.update({"Hepin": 99 }) # Updating value for existing key
print(marks) # Updated dictionary with new value for existing key

print(marks.get("Nirdesh1")) # Accessing a non-existing key returns None
print(marks["Nirdesh1"]) # Accessing a non-existing key raises a KeyError
