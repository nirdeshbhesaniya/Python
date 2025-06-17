def goodday(name,ending="Thanks"):
    print(f"Good day, {name}")
    print(ending)
    return "OK"

# Function Call
goodday("Nirdesh","Thank you!")
goodday("Harshil    ")  # This will print None since goodday does not return anything