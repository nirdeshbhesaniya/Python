n = int(input("Enter a number: "))

i = 2
while (i<=n):
    if(n%i)==0:
        print("This is not prime number")
        break
    i += 1
else:
    print("This is a prime number")