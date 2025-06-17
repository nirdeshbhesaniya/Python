# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# Function Definition

def average():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    c = int(input("Enter your third number: "))
    
    avg = (a + b + c) / 3
    print(f"The average of {a}, {b}, and {c} is: {avg}")
    
# Function Call

average()
print("Function executed successfully.")
