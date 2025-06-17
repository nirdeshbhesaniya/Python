try:
    a = int(input("Enter number a: "))
    b = int(input("Enter number n:"))
    
    print(a/b)
except ZeroDivisionError as e:
    print("Infinite")