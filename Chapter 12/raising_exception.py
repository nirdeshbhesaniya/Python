a = int(input("Enter Number:"))
b = int(input("Enter Second Number:"))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")