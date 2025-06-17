str = "Nirdesh"

print(len(str))  # Output: 7
print(str.endswith("sh"))
print(str.endswith("sH"))  # Output: False
print(str.startswith("Nir"))  # Output: True
print(str.count("i"))  # Output: 1

capitalize_string = str.capitalize() # Capitalizes the first character
print(capitalize_string)  # Output: Nirdesh

index  =  str.index("d")  # Returns the index of the first occurrence of "d"
print(index)  # Output: 3

Replece_string = str.replace("Nirdesh", "Nirdesh Bhesaniya")
print(Replece_string)  # Output: Nirdesh Bhesaniya