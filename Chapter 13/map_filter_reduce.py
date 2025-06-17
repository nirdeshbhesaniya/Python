from functools import reduce
# Map Example 
l = [1,2,3,4,5]

square = lambda x:x*x

squList = map(square,l)
print(list(squList))

# Filter Example 

def even(n):
    if(n%2 == 0):
        return True
    return False

evenList = filter(even,l)

print(list(evenList))

# Reduce Example 

def sum(a,b):
    return a+b

mul = lambda x,y:x*y


print(reduce(sum, l))
print(reduce(mul, l))