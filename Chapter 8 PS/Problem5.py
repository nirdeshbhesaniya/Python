def pattern(n):
    if n == 0:
        return
    print(n * "*")
    pattern(n - 1)
    
n = int(input("Enter a number: "))
pattern(n)  # Output: Pattern of asterisks from n to 1