#  Write a program to sum a list with 4 numbers.
numbers = []
numbers.append(int(input("Enter number 1: ")))
numbers.append(int(input("Enter number 2: ")))
numbers.append(int(input("Enter number 3: ")))
numbers.append(int(input("Enter number 4: ")))
sum_of_numbers = sum(numbers)
print("The sum of the numbers is:", sum_of_numbers)
